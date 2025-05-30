from dataclasses import dataclass
from typing import Optional

@dataclass
class ChatRequest:
    message: str

    @staticmethod
    def from_dict(data: dict) -> tuple[Optional['ChatRequest'], Optional[str]]:
        message = data.get("message")
        if not message:
            return None, "Повідомлення не надано"
        if not isinstance(message, str):
            return None, "Повідомлення має бути рядком"
        return ChatRequest(message=message), None