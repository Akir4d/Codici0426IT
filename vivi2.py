from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1024
)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Ciao, chi sei?",
    config=config
)

print(response.text)