from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.interview_routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/interview")


@app.get("/")
def root():
    return {"message": "Interview Chatbot API running"}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from models.schemas import QuestionRequest, AnswerRequest
# from services.gemini_service import generate_question, evaluate_answer

# app = FastAPI()

# # Allow frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # restrict in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def root():
#     return {"message": "Interview AI API running"}


# @app.post("/generate-question")
# def get_question(req: QuestionRequest):
#     question = generate_question(req.role, req.difficulty)
#     return {"question": question}


# @app.post("/evaluate-answer")
# def eval_answer(req: AnswerRequest):
#     feedback = evaluate_answer(req.question, req.answer)
#     return {"feedback": feedback}