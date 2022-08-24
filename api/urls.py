from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.note_views import Notes, NoteDetail
from .views.folder_views import Folders, FolderDetail

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),

    path('notes/', Notes.as_view(), name='notes'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note_detail'),

    path('folders/', Folders.as_view(), name='folders'),
    path('folders/<int:pk>/', FolderDetail.as_view(), name='folder_detail'),



    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
