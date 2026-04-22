class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, user, bot):
        self.history.append({"user": user, "bot": bot})

    def get_context(self):
        return "\n".join(
            [f"User: {h['user']} \nBot: {h['bot']}" for h in self.history]
        )