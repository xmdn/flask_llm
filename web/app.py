import os
from flask import Flask
from common.services.chat_service import ChatService
from common.controllers.chat_controller import ChatController

from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
CORS(app)

chat_service = ChatService(openai_api_key=os.getenv("OPENAI_API_KEY"))
chat_controller = ChatController(chat_service)

app.route("/chat", methods=["POST"])(chat_controller.chat)
app.route("/reset", methods=["POST"])(chat_controller.reset)
app.route('/history', methods=['GET'])(chat_controller.history)

if __name__ == "__main__":
    app.run(debug=True)

