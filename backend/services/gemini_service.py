import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3-flash-preview")


def generate_questions(role, difficulty):
    prompt = f"""
    Generate exactly 15 interview questions for a {role}.
    Difficulty: {difficulty}.

    Return ONLY as a numbered list.
    """
    res = model.generate_content(prompt)
    text = res.text

    questions = []
    for line in text.split("\n"):
        if line.strip():
            questions.append(line.split(".", 1)[-1].strip())

    return questions[:15]


def generate_closing():
    return "Thank you for attending the interview. We will get back to you soon."
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-3-flash-preview")


# def generate_question(role: str, difficulty: str):
#     prompt = f"""
#     Generate one interview question for a {role}.
#     Difficulty: {difficulty}.
#     Only return the question.
#     """
#     res = model.generate_content(prompt)
#     return res.text.strip()


# def evaluate_answer(question: str, answer: str):
#     prompt = f"""
#     You are an interviewer.

#     Question: {question}
#     Answer: {answer}

#     Respond in JSON:
#     {{
#       "score": "",
#       "strengths": "",
#       "weaknesses": "",
#       "improvement": "",
#       "ideal_answer": ""
#     }}
#     """
#     res = model.generate_content(prompt)
#     return res.text