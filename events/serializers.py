from pyexpat import model
from rest_framework import serializers
from events.models import Event, EventMember

class TimeSlotSerializer(serializers.ListField):
    slot = serializers.DateTimeField() 

class EventMemberSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EventMember
        fields = ['id', 'availability', 'username', 'event']

class EventSerializer(serializers.ModelSerializer):

    event_members = EventMemberSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'start_date', 'end_date', 'event_members']
        read_only_fields = ['id', 'event_members']       

class EventMemberCreateSerializer(serializers.ModelSerializer):

    class Meta: 
        model = EventMember
        fields = ['id', 'availability', 'username', 'event', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        read_only_fields = ['id', 'availability']

class EventMemberUpdateSerializer(serializers.ModelSerializer):
    change_to_available = serializers.BooleanField()
    timeslots = TimeSlotSerializer(required=False)

    class Meta: 
        model = EventMember
        fields = ['event', 'username', 'change_to_available', 'timeslots']