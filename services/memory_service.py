from collections import deque


class MemoryService:

    def __init__(
        self,
        max_turns=20
    ):

        self.history = deque(
            maxlen=max_turns
        )

    def add_user(
        self,
        content
    ):

        self.history.append(
            {
                "role": "user",
                "content": content
            }
        )

    def add_assistant(
        self,
        content
    ):

        self.history.append(
            {
                "role": "assistant",
                "content": content
            }
        )

    def get_context(self):

        return list(
            self.history
        )

    def clear(self):

        self.history.clear()