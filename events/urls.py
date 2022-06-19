from django.urls import path
from .views import ( CreateEventView,
EventList, EventDetailView,
DeleteEventView, EditEventView,
CommentEventView
)
urlpatterns = [
    path('create/', CreateEventView.as_view(), name="create_event"),
    path('events/', EventList.as_view(), name='events'),
    path('view/<slug:pk>/', EventDetailView.as_view(), name="view_event"),
    path('edit/<slug:pk>/', EditEventView.as_view(), name="edit_event"),
    path('delete/<slug:pk>/', DeleteEventView.as_view(), name="delete_event"),
    path('comment/<slug:pk>/', CommentEventView.as_view(), name="comment_event"), 
]
