import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GROK_API_KEY = os.getenv("GROK_API_KEY")

MAX_MEMORY_TURNS = 20