import uuid

from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
    feedbackId: str = str(uuid.uuid4())
    userId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    feedbackText: str
    rating: int
    createdAt: datetime = datetime.utcnow()