import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(prompt: str) -> str:
    """
    Sends a prompt to OpenAI's GPT-4 and returns the response text.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Switch to "gpt-3.5-turbo" if needed
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[ERROR] GPT call failed: {e}"

