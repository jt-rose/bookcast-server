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

class CastingSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Casting
        fields = ['created', 'creator', 'source_name', 'source_image_url', 'description']
    def create(self, validated_data):
        return Casting.objects.create(**validated_data)

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['casting', 'name', 'actor', 'description', 'photo_url']

class CastingVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting_Vote
        fields = ['user', 'casting', 'like', 'comment']
        
class CharacterVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_Vote
        fields = ['user', 'character', 'like', 'comment']