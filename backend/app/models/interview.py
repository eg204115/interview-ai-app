import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Interview(BaseModel):
    interviewId:  str = str(uuid.uuid4())
    userId: str = str(uuid.uuid4())
    title: str
    description: Optional[str]
    jobPosition: str
    difficulty: str
    startTime: Optional[datetime]
    endTime: Optional[datetime]
    status: str
    totalQuestions: int