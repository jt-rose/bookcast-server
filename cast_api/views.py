# from django.shortcuts import render

# Create your views here.
from cast_api.permissions import IsCreatorOrReadOnly
from rest_framework import generics
from .serializers import UserSerializer
from .serializers import CastingSerializer
from .serializers import CharacterSerializer
from .serializers import CastingVoteSerializer
from .serializers import CharacterVoteSerializer
from django.contrib.auth.models import User
from .models import Casting
from .models import Character
from .models import Casting_Vote
from .models import Character_Vote
from rest_framework import permissions

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class CastingList(generics.ListCreateAPIView):
    queryset = Casting.objects.all()
    serializer_class = CastingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    
class CastingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Casting.objects.all().order_by('id')
    serializer_class = CastingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
    


class CastingVoteList(generics.ListCreateAPIView):
    queryset = Casting_Vote.objects.all()
    serializer_class = CastingVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CastingVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Casting_Vote.objects.all().order_by('id')
    serializer_class = CastingVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

class CharacterVoteList(generics.ListCreateAPIView):
    queryset = Character_Vote.objects.all()
    serializer_class = CharacterVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CharacterVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character_Vote.objects.all().order_by('id')
    serializer_class = CharacterVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]