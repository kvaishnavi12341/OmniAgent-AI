import requests
from app.config import settings
from app.memory.conversation_memory import ConversationMemory

class ConversationAgent:
    def __init__(self):
        self.memory = ConversationMemory()

    def respond(self, user_input):
        context = self.memory.get_context()

        prompt = f"""
        You are a helpful AI assistant.

        Context:
        {context}

        User: {user_input}
        """

        response = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={"model": settings.OLLAMA_MODEL, "prompt": prompt, "stream": False},
        ).json()

        output = response.get("response", "")
        self.memory.add(user_input, output)

        return output