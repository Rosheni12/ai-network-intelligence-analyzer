import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Write one sentence about cybersecurity.")

print("TEXT:")
print(repr(response.text))

print("\nFULL RESPONSE:")
print(response)