import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    prompt_tokens, response_tokens = generate_content(client, messages)

    if "--verbose" in user_prompt:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    return (prompt_tokens, response_tokens)


if __name__ == "__main__":
    main()
