from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Access your environment variable
api_key = os.getenv('API_KEY')

print(api_key)
