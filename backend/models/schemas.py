from pydantic import BaseModel
from typing import List, Optional

class StartInterviewRequest(BaseModel):
    role: str
    difficulty: str


class AnswerRequest(BaseModel):
    interview_id: str
    answer: str


class Interview(BaseModel):
    role: str
    difficulty: str
    questions: List[str]
    answers: List[str]
    current_index: int
    completed: bool