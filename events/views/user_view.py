

from rest_framework import generics
from django.contrib.auth import get_user_model
from events.serializers import user_serializer

User = get_user_model()


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializer.UserSerializer