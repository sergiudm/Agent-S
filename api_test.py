import os
import httpx  # Keep httpx import if you might use it explicitly later, but not needed for this example
from openai import OpenAI
import openai

# 1. Verify API Key (optional: print for debugging, then remove)
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    print("Error: OPENROUTER_API_KEY environment variable not set.")
    exit()
# print(f"Loaded API Key starting with: {api_key[:5]}")


# 2. Initialize Client (try without custom http_client first)
client = OpenAI(
    api_key=api_key,
    base_url="https://api.openrouter.ai/v1",
    # If the above fails with SSL issues AND you are NOT behind a proxy,
    # you could try reinstating the http_client with verify=False,
    # but it's better to solve the underlying SSL issue.
    # http_client=httpx.Client(verify=False),
)

try:
    print("Attempting to call OpenRouter API...")
    response2 = client.chat.completions.create(
        # 3. Use a known valid model name (try 'openai/gpt-4o' or 'openai/gpt-3.5-turbo')
        model="openai/gpt-4o",  # Or "openai/gpt-3.5-turbo"
        messages=[
            {
                "role": "user",
                "content": "我要有研究推理模型与非推理模型区别的课题，怎么体现我的专业性",
            }
        ],
    )
    # 4. Correct attribute access for content
    print("API Call Successful!")
    print(response2.choices[0].message.content)

except openai.APIConnectionError as e:
    print(f"API Connection Error: {e}")
    print(f"Underlying error type: {type(e.__cause__)}")
    print(f"Underlying error details: {e.__cause__}")
except openai.APIStatusError as e:
    print(f"OpenAI API returned an API Error: {e.status_code} - {e.message}")
    print(f"Response: {e.response.text}")
except openai.APIError as e:
    print(f"OpenAI API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    import traceback

    traceback.print_exc()
