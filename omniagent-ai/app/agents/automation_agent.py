class AutomationAgent:
    def run(self, classification,context=None):
        #if classification["category"] == "system" and context:
        if classification.get("category") == "system" and context:
            return f"SOP Applied: {context}"

        return "No automation needed" 