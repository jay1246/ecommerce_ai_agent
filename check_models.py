import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("\nAvailable Models:")
for i, model in enumerate(genai.list_models(), 1):
    print(f"{i}. {model.name}")

print("\nRecommended model: gemini-pro")