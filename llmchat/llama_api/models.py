import uuid

from django.db import models
from django.contrib.auth.models import User
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelArrayField


class Message(EmbeddedModel):

    class Role(models.TextChoices):
        SYSTEM = "system", "System"
        USER = "user", "User"
        ASSISTANT = "assistant", "Assistant"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    role = models.CharField(max_length=16, choices=Role.choices)
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, blank=True)
    messages = EmbeddedModelArrayField(Message, default=list, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


