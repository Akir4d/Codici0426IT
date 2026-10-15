from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1024,
    system_instruction="""Sei un cane e rispondi sempre come un cane.
    Se ti viene chiesto qualcosa che non riguarda i cani, rispondi con 'Woof woof!'
    """
)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Ciao, chi sei?",
    config=config
)

print(response.text)