# from django.shortcuts import render

# Create your views here.
from cast_api.permissions import IsCreatorOrReadOnly
from rest_framework import generics
from .serializers import CastingCommentSerializer, CharacterCommentSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from .serializers import CastingSerializer
from .serializers import CharacterSerializer
from .serializers import CastingVoteSerializer
from .serializers import CharacterVoteSerializer
from django.contrib.auth.models import User
from .models import Casting, Casting_Comment, Character_Comment
from .models import Character
from .models import Casting_Vote
from .models import Character_Vote
from rest_framework import permissions
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

from knox.models import AuthToken

# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

# Get User API
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

#@method_decorator(csrf_protect, name='dispatch')
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
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class CastingVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Casting_Vote.objects.all().order_by('id')
    serializer_class = CastingVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
    

class CharacterVoteList(generics.ListCreateAPIView):
    queryset = Character_Vote.objects.all()
    serializer_class = CharacterVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class CharacterVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character_Vote.objects.all().order_by('id')
    serializer_class = CharacterVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
    
# comments

class CastingCommentList(generics.ListCreateAPIView):
    queryset = Casting_Comment.objects.all()
    serializer_class = CastingCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CastingCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Casting_Comment.objects.all().order_by('id')
    serializer_class = CastingCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

class CharacterCommentList(generics.ListCreateAPIView):
    queryset = Character_Comment.objects.all()
    serializer_class = CharacterCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CharacterCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character_Comment.objects.all().order_by('id')
    serializer_class = CharacterCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]