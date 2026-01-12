from ..models import Conversation, Message
from ..dto import MessageAndReplyDTO
from .llm_model import generate_llm_response
from django.shortcuts import get_object_or_404


class MessageService():
    
    @staticmethod
    def process_and_save(messageDTO):
        conversation = get_object_or_404(
            Conversation,
            id=messageDTO.conversation_id
        )

        prompt_message = Message(text=messageDTO.text, role=Message.Role.USER)
        conversation.messages.append(prompt_message)

        reply_message = Message(text=generate_llm_response(conversation.messages), role=Message.Role.ASSISTANT)
        conversation.messages.append(reply_message)
        
        conversation.save(update_fields=["messages"])

        return MessageAndReplyDTO(
            reply=reply_message.text,
            prompt_created_at=prompt_message.created_at,
            reply_created_at=reply_message.created_at
        )
