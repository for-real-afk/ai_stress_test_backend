BLOCKED_WORDS = [

    "bomb",

    "ransomware",

    "steal passwords",

    "hack wifi",

    "malware"
]


class SafetyGuardrails:

    @staticmethod
    def check(prompt):

        prompt = prompt.lower()

        for word in BLOCKED_WORDS:

            if word in prompt:

                return False

        return True