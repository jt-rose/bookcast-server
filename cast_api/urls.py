from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='user_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/castings/', views.CastingList.as_view()),
    path('api/castings/<int:pk>/', views.CastingDetail.as_view()),
    path('api/characters/', views.CharacterList.as_view()),
    path('api/characters/<int:pk>/', views.CharacterDetail.as_view()),
    path('api/castingvotes/', views.CastingVoteList.as_view()),
    path('api/castingvotes/<int:pk>/', views.CastingVoteDetail.as_view()),
    path('api/charactervotes/', views.CharacterVoteList.as_view()),
    path('api/charactervotes/<int:pk>/', views.CharacterVoteDetail.as_view())
]