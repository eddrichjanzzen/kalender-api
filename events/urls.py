from django.urls import path
from events.views import EventListCreateView, EventDetailView, EventMemberCreateView, EventMemberRetrieveUpdateView
EventMemberCreateView
urlpatterns = [
    path('events/', EventListCreateView.as_view()),
    path('events/<uuid:pk>', EventDetailView.as_view()),
    path('eventmembers', EventMemberCreateView.as_view()),
    path('eventmembers/<uuid:pk>', EventMemberRetrieveUpdateView.as_view())
]