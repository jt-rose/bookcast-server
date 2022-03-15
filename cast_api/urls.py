from django.urls import path
from . import views

urlpatterns = [
    path('api/users', views.UserList.as_view(), name='user_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'), # api/contacts will be routed to the ContactDetail view for handling
]