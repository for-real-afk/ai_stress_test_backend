from abc import ABC
from abc import abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        context: list
    ) -> str:
        passs