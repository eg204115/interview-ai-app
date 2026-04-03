from fastapi import APIRouter
from models.schemas import StartInterviewRequest, AnswerRequest
from services.interview_service import start_interview, submit_answer

router = APIRouter()


@router.post("/start")
def start(req: StartInterviewRequest):
    interview_id, first_question = start_interview(req.role, req.difficulty)

    return {
        "interview_id": interview_id,
        "question": first_question
    }


@router.post("/answer")
def answer(req: AnswerRequest):
    result = submit_answer(req.interview_id, req.answer)
    return result