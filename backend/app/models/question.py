from pydantic import BaseModel
import uuid

from backend.app.core.enums import DifficultyLevel

class Question(BaseModel):
    questionId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    questionText: str
    questionType: DifficultyLevel
    sequenceNumber: int
    timeLimit: int
    difficulty: str