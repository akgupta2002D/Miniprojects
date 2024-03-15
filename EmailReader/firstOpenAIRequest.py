import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('API_KEY'))


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Write three lines of fun poem"}
    ]
)

print(completion.choices[0].message)
