from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.note import Note
from ..serializers import NoteSerializer
from ..models.folder import Folder
from ..serializers import FolderSerializer

# Create your views here.
class Folders(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = FolderSerializer
    def get(self, request):
        """Index request"""
        # Get all the folders:
        # and order them by updated
        folder = Folder.objects.filter(owner=request.user.id).order_by('-updated')
        # Run the data through the serializer
        data = FolderSerializer(folder, many=True).data
        return Response({ 'folders': data })

    def post(self, request):
        """Create request"""
        
        if(request.data["folder"]["name"] == ""):
            request.data["folder"]["name"] = "Unnamed Folder"

        if(request.data["folder"]["description"] == ""):
            request.data["folder"]["description"] = "No Description"

        print("data: ", request.data)

        # Add user to request data object
        request.data['folder']['owner'] = request.user.id
        # Serialize/create folder
        folder = FolderSerializer(data=request.data['folder'])
        # If the folder data is valid according to our serializer...
        if folder.is_valid():
            # Save the created folder & send a response
           folder.save()
           return Response({ 'folder': folder.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(folder.errors, status=status.HTTP_400_BAD_REQUEST)

class FolderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the folder to show
        folder = get_object_or_404(Folder, pk=pk)
        # Only want to show owned folders?
        if request.user != folder.owner:
            raise PermissionDenied('Unauthorized, you do not own this folder')
        # print("folder: ",folder.notes.all())
        # Run the data through the serializer so it's formatted
        data = FolderSerializer(folder).data
        notes = folder.notes.all()
        data2 = NoteSerializer(notes, many=True).data
        # print("data: ", data)
        # print("data2: ", data2)
        return Response({ 'folder': data, 'notes': data2})

    def delete(self, request, pk):
        """Delete request"""
        # Locate folder to delete
        folder = get_object_or_404(Folder, pk=pk)
        # Check the folder's owner against the user making this request
        if request.user != folder.owner:
            raise PermissionDenied('Unauthorized, you do not own this folder')
        # Only delete if the user owns the folder
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate folder
        # get_object_or_404 returns a object representation of our folder
        folder = get_object_or_404(Folder, pk=pk)
        # Check the folder's owner against the user making this request
        if request.user != folder.owner:
            raise PermissionDenied('Unauthorized, you do not own this folder')

        # Ensure the owner field is set to the current user's ID
        request.data['folder']['owner'] = request.user.id
        print(request.data["folder"])
        
        # Validate updates with serializer
        data = FolderSerializer(folder, data=request.data['folder'], partial=True)
        # print("data: ", data)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
