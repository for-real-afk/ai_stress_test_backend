import google.generativeai as genai

from providers.base import BaseProvider

from config import GEMINI_API_KEY


genai.configure(
    api_key=GEMINI_API_KEY
)


class GeminiProvider(BaseProvider):

    def __init__(self):

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(
        self,
        prompt,
        context
    ):

        history = ""

        for item in context:

            history += (
                f"{item['role']}: "
                f"{item['content']}\n"
            )

        full_prompt = f"""
Conversation History:

{history}

User:
{prompt}

Assistant:
"""

        response = self.model.generate_content(
            full_prompt
        )

        return response.text