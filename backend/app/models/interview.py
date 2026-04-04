import uuid

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from backend.app.core.enums import DifficultyLevel

class Interview(BaseModel):
    interviewId:  str = str(uuid.uuid4())
    userId: str = str(uuid.uuid4())
    title: str
    description: Optional[str]
    jobPosition: str
    difficulty: DifficultyLevel
    startTime: Optional[datetime]
    endTime: Optional[datetime]
    status: str
    totalQuestions: int