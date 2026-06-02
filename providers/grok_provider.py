from openai import OpenAI
import os

from providers.base import BaseProvider


class GroqProvider(BaseProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    def generate(
        self,
        prompt,
        context
    ):

        messages = []

        for item in context:
            messages.append(
                {
                    "role": item["role"],
                    "content": item["content"]
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.4
        )

        return response.choices[0].message.content