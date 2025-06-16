import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOGETHER_API_KEY")

if not api_key:
    raise ValueError("TOGETHER_API_KEY is not set")

openaiClient = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)

message = "Hello, this is my first message to you."
response = openaiClient.chat.completions.create(model="meta-llama/Llama-Vision-Free", messages=[{"role": "user", "content": message}])
print(response.choices[0].message.content)