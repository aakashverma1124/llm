import os
import openai
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

api_key = os.getenv("TOGETHER_API_KEY")

if not api_key:
    raise ValueError("TOGETHER_API_KEY is not set")

openaiClient = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    """
    Create this Website object from the given url using the BeautifulSoup library
    """
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body("script", "style", "img", "input"):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
    
    
innoskrit = Website("https://innoskrit.in")
# print(innoskrit.title)
# print(innoskrit.text)

"""
You may know this already - but if not, you will get very familiar with it!
Models like GPT4o have been trained to receive instructions in a particular way.
They expect to receive:
A system prompt that tells them what task they are performing and what tone they should use
A user prompt -- the conversation starter that they should reply to
"""

system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, ignoring text that might be navigation related. Respond in markdown."

def user_prompt_for_website(website: Website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# print(user_prompt_for_website(innoskrit))

"""
Messages:
The API from OpenAI expects to receive messages in a particular structure. Many of the other APIs share this structure:

``` [ {"role": "system", "content": "system message goes here"}, {"role": "user", "content": "user message goes here"} ]

To give you a preview, the next 2 cells make a rather simple call - we won't stretch the mighty GPT (yet!)
"""

response = openaiClient.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt_for_website(innoskrit)}],
    response_format={"type": "text"}
)

print(response.choices[0].message.content)