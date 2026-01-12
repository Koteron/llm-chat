from rest_framework import serializers
from .models import Conversation
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    id = serializers.CharField(read_only=True) 

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = tuple(UserCreateSerializer.Meta.fields) + ('id',)

class CustomUserSerializer(UserSerializer):
    id = serializers.CharField(read_only=True) 

    class Meta(UserSerializer.Meta):
        model = User
        fields = tuple(UserSerializer.Meta.fields) + ('id',)

class AddMessageSerializer(serializers.Serializer):
    conversation_id = serializers.UUIDField()
    text = serializers.CharField(max_length=1024)
    created_at = serializers.DateTimeField(read_only=True)

class MessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    role = serializers.CharField(max_length=16)
    created_at = serializers.DateTimeField(read_only=True)
    
class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        exclude = ["user"]
        read_only_fields = ['messages', 'created_at', 'updated_at']

class ConversationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        exclude = ["user", "messages"]
        read_only_fields = ['created_at', 'updated_at']