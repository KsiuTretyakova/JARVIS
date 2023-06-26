from dotenv import load_dotenv as ld
import os
import openai

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

# openai.api_key = "KEY"
# openai.api_key = input()

openai.api_key = os.getenv("api_key")
