from django.urls import path
from .views import NoteViewManual

urlpatterns = [
    path('', NoteViewManual.as_view(), name='note-create'),  # Ensure correct URL pattern
]
