import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Conversation(BaseModel):
    conversationId: str = str(uuid.uuid4())
    userId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    startTime: datetime = datetime.utcnow()
    endTime: Optional[datetime]
    conversationTopic: Optional[str]