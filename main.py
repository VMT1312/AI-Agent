import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

res = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=sys.argv[1]
)

print(res.text)

prompt_token_count = res.usage_metadata.prompt_token_count
candidates_token_count = res.usage_metadata.candidates_token_count

print(f"Prompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}")