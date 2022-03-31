from django.urls import path
from events.views import user_view 

urlpatterns = [
    path('users/', user_view.UserList.as_view()),
    path('users/<uuid:user_id>', user_view.UserDetail.as_view()),
]