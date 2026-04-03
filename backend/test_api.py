from google import genai
import os
from dotenv import load_dotenv
# from google.genai import errors # Import errors for handling

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

question = input("Ask something: ")

try:
    response = client.models.generate_content(
        model=model_name,
        contents=question
    )
    print(response.text)
    print(response.model_dump_json(exclude_none=True, indent=4))

# except errors.ServerError as e:
#     print(f"Server is busy or unavailable (503). Try again in a few seconds.")
#     print(f"Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")