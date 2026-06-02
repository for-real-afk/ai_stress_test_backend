from transformers import pipeline

from providers.base import BaseProvider


class QwenProvider(BaseProvider):

    def __init__(self):

        self.pipe = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct"
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

        final_prompt = f"""
{history}

user:
{prompt}

assistant:
"""

        result = self.pipe(
            final_prompt,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7
        )

        return result[0]["generated_text"]