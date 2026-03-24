from pydantic import BaseModel

class QuestionRequest(BaseModel):
    role: str
    difficulty: str


class AnswerRequest(BaseModel):
    question: str
    answer: str