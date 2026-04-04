import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Answer(BaseModel):
    answerId: str = str(uuid.uuid4())
    questionId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    answerText: str
    submittedAt: datetime = datetime.utcnow()
    durationSeconds: int
    score: Optional[float] = None   