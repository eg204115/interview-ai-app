import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from backend.app.core.enums import SenderType

class Message(BaseModel):
    messageId: str = str(uuid.uuid4())
    conversationId: str = str(uuid.uuid4())
    senderType: SenderType  # "user" or "assistant"
    messageText: str
    timestamp: datetime = datetime.utcnow()
    sentiment: Optional[str]