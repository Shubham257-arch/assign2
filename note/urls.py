from django.urls import path
from .views import NoteViewManual, NoteGetOneView

urlpatterns = [
    path('', NoteViewManual.as_view(), name='create'),
    path('<int:note_id>/', NoteGetOneView.as_view(), name='note-get-one'),
]
