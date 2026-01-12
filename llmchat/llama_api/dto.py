from dataclasses import dataclass
import uuid
import datetime

@dataclass
class MessageDTO:
    conversation_id: uuid 
    text: str
    
@dataclass
class MessageAndReplyDTO:
    prompt_created_at: datetime 
    reply: str
    reply_created_at: datetime 
    