from rest_framework import serializers 
from .models import Casting
from .models import Character
from .models import Casting_Vote
from .models import Character_Vote
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    castings = serializers.PrimaryKeyRelatedField(many=True, queryset=Casting.objects.all())
    creator = serializers.ReadOnlyField(source='creator.username')
    casting_votes = serializers.PrimaryKeyRelatedField(many=True, queryset=Casting_Vote.objects.all())
    character_votes = serializers.PrimaryKeyRelatedField(many=True, queryset=Character_Vote.objects.all())
    class Meta:
        model = User # tell django which model to use
        fields = ['id', 'username', 'email', 'password', 'creator', 'castings', 'casting_votes', 'character_votes'] # hide password
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

class CharacterVoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Character_Vote
        fields = ['user', 'character', 'id', 'like', 'comment']

class CharacterSerializer(serializers.ModelSerializer):
    votes_and_comments = CharacterVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ['casting', 'id', 'name', 'votes_and_comments', 'actor', 'description', 'photo_url']

class CastingVoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Casting_Vote
        fields = ['user', 'casting', 'id', 'like', 'comment']
        
class CastingSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    characters = CharacterSerializer(many=True, read_only=True)
    votes_and_comments = CastingVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Casting
        fields = ['created', 'id', 'creator', 'characters', 'votes_and_comments', 'source_name', 'source_image_url', 'description']
    def create(self, validated_data):
        print(validated_data)
        return Casting.objects.create(**validated_data)

