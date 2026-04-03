import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

model = genai.GenerativeModel(model_name)

question = input("Ask something: ")

response = model.generate_content(question)

print("\nAnswer:\n", response.text)