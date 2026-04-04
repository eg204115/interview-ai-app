import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InterviewSession(BaseModel):
    sessionId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    sessionStart: datetime = datetime.utcnow()
    sessionEnd: Optional[datetime]
    deviceInfo: Optional[str]
    ipAddress: Optional[str]
    status: str