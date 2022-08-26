from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.note import Note
from ..serializers import NoteSerializer

# Create your views here.
class Notes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = NoteSerializer
    def get(self, request):
        """Index request"""
        # Get all the notes:
        # and order them by updated
        notes = Note.objects.filter(owner=request.user.id).order_by('-updated')
        # Run the data through the serializer
        data = NoteSerializer(notes, many=True).data
        return Response({ 'notes': data })

    def post(self, request):
        
        """Create request"""
        # Add user to request data object
        request.data['note']['owner'] = request.user.id
        print("request.data['note']: ", request.data['note'])
        if(request.data["note"]["title"] == None):
            request.data["note"]["title"] = "unnamed note"
        if(request.data["note"]["body"] == None):
            request.data["note"]["body"] = ""
        # Serialize/create note
        note = NoteSerializer(data=request.data['note'])
        # If the note data is valid according to our serializer...
        if note.is_valid():
            # Save the created note & send a response
           note.save()
           return Response({ 'note': note.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the note to show
        note = get_object_or_404(Note, pk=pk)
        # Only want to show owned notes?
        if request.user != note.owner:
            raise PermissionDenied('Unauthorized, you do not own this note')

        # Run the data through the serializer so it's formatted
        data = NoteSerializer(note).data
        return Response({ 'note': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate note to delete
        note = get_object_or_404(Note, pk=pk)
        # Check the note's owner against the user making this request
        if request.user != note.owner:
            raise PermissionDenied('Unauthorized, you do not own this note')
        # Only delete if the user owns the note
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Note
        # get_object_or_404 returns a object representation of our Note
        note = get_object_or_404(Note, pk=pk)
        # Check the note's owner against the user making this request
        if request.user != note.owner:
            raise PermissionDenied('Unauthorized, you do not own this note')

        # Ensure the owner field is set to the current user's ID
        request.data['note']['owner'] = request.user.id
        # Validate updates with serializer
        data = NoteSerializer(note, data=request.data['note'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
