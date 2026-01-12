from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import ConversationDetailSerializer, ConversationListSerializer, AddMessageSerializer
from .models import Conversation
from .services.services import MessageService
from .dto import MessageDTO


class MessageView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddMessageSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message_and_reply_dto = MessageService.process_and_save(
            messageDTO=MessageDTO(
                conversation_id=serializer.validated_data["conversation_id"],
                text=serializer.validated_data["text"]
            )
        )

        return Response({
            "reply": message_and_reply_dto.reply,
            "prompt_created_at": message_and_reply_dto.prompt_created_at,
            "reply_created_at": message_and_reply_dto.reply_created_at,
        })


class ConversationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        queryset = Conversation.objects.filter(user=self.request.user)
        if self.action == "list":
            return queryset.defer("messages")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return ConversationListSerializer
        return ConversationDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
