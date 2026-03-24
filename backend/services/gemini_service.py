import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")


def generate_question(role: str, difficulty: str):
    prompt = f"""
    Generate one interview question for a {role}.
    Difficulty: {difficulty}.
    Only return the question.
    """
    res = model.generate_content(prompt)
    return res.text.strip()


def evaluate_answer(question: str, answer: str):
    prompt = f"""
    You are an interviewer.

    Question: {question}
    Answer: {answer}

    Respond in JSON:
    {{
      "score": "",
      "strengths": "",
      "weaknesses": "",
      "improvement": "",
      "ideal_answer": ""
    }}
    """
    res = model.generate_content(prompt)
    return res.text