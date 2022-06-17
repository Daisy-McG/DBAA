from django.urls import path
from .views import CreateEventView, EventList, EventDetailView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name="create_event"),
    path('events/', EventList.as_view(), name='events'),
    path('view/<slug:pk>/', EventDetailView.as_view(), name="view_event"),
]
