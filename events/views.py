from rest_framework import generics, status
from events import serializers
from events.models import Event, EventMember
from rest_framework.response import Response

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.EventSerializer
    queryset =  Event.objects.all()

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EventSerializer
    queryset =  Event.objects.all()

class EventMemberCreateView(generics.CreateAPIView):
    queryset = EventMember.objects.all()
    serializer_class = serializers.EventMemberCreateSerializer

class EventMemberRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = EventMember.objects.all()
    serializer_class = serializers.EventMemberSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.EventMemberUpdateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)        

        user_data = self.get_serializer(instance)

        return Response(user_data.data, status=status.HTTP_200_OK)
