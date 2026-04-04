from pydantic import BaseModel
import uuid

class Question(BaseModel):
    questionId: str = str(uuid.uuid4())
    interviewId: str = str(uuid.uuid4())
    questionText: str
    questionType: str
    sequenceNumber: int
    timeLimit: int
    difficulty: str