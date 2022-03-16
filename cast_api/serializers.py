from rest_framework import serializers 
from .models import Casting
from .models import Character
from .models import Casting_Vote
from .models import Character_Vote
from django.contrib.auth.models import User



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

class CastingSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='user')
    class Meta:
        model = Casting
        fields = ['created', 'id', 'creator', 'source_name', 'source_image_url', 'description']
    def create(self, validated_data):
        print(validated_data)
        return Casting.objects.create(**validated_data)

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['casting', 'id', 'name', 'actor', 'description', 'photo_url']

class CastingVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting_Vote
        fields = ['user', 'casting', 'id', 'like', 'comment']
        
class CharacterVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_Vote
        fields = ['user', 'character', 'id', 'like', 'comment']