from typing import Tuple, Optional
from openai import OpenAI

class ChatService:
    def __init__(self, openai_api_key: str):
        self.client = OpenAI(api_key=openai_api_key)
        self.chat_history = []

    def process_chat(self, user_message: str) -> Tuple[Optional[str], Optional[str]]:
        self.chat_history.append({"role": "user", "content": user_message})

        messages = [
        {"role": "system", "content": "Ви веселий, гумористичний помічник. Відповідайте з гумором, але все одно корисно."}
        ] + self.chat_history

        try:
            response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages
            )
            reply = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": reply})
            return reply, None
        except Exception as e:
            return None, str(e)

    def reset_chat(self) -> None:
        self.chat_history = []