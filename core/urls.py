from django.urls import path
from core.views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<uuid:pk>', UserDetail.as_view()),
]