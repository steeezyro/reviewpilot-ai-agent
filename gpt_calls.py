import os
import requests
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# Primary and fallback models
PRIMARY_MODEL = "nvidia/llama-3.3-nemotron-super-49b-v1:free"
FALLBACK_MODEL = "arliai/qwq-32b-rpr-v1:free"

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def send_request(prompt: str, model: str):
    try:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        # Debug print full response if unexpected format
        if "choices" not in data:
            print(f"[DEBUG] Full response (no 'choices'): {data}")
            return None

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError as http_err:
        print(f"[ERROR] GPT call failed: {http_err}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected GPT call error: {e}")
        return None

def call_gpt(prompt: str):
    # Try primary model first
    result = send_request(prompt, PRIMARY_MODEL)
    if result is not None:
        return result

    print("🔁 Primary model failed. Switching to fallback model...")

    # Try fallback model
    result = send_request(prompt, FALLBACK_MODEL)
    if result is not None:
        return result

    return "[ERROR] Both primary and fallback GPT models failed."
