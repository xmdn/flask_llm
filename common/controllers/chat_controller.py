from flask import jsonify, request
from common.models.chat_request import ChatRequest
from common.services.chat_service import ChatService

class ChatController: 
    def __init__(self, chat_service: ChatService): 
        self.chat_service = chat_service 

    def chat(self): 
        data = request.get_json() 
        chat_request, error = ChatRequest.from_dict(data) 
        if error: 
            return jsonify({"error": error}), 400 

        reply, error = self.chat_service.process_chat(chat_request.message) 
        if error: 
            return jsonify({"error": error}), 500 

        return jsonify({"reply": reply})
    
    def history(self):
        return jsonify({"history": self.chat_service.chat_history})

    def reset(self): 
        self.chat_service.reset_chat() 
        return jsonify({"status": "context cleared"})