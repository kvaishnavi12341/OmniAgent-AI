import requests
from app.config import settings


class ClassificationAgent:
    def classify(self, text):
        prompt = f"""
Classify the following into:
severity: P1/P2/P3/P4
category: safety/illegal/system/normal

Text: {text}

Return JSON.
"""

        try:
            response = requests.post(
                f"{settings.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": settings.OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )

            data = response.json()
            res = data.get("response", "").lower()

        except Exception as e:
            print("LLM ERROR:", e)
            return {"severity": "P3", "category": "normal"}  # ✅ fallback

        # ✅ SAFE RULE-BASED INTERPRETATION
        if any(word in res for word in ["p1", "attack", "knife", "danger", "threat"]):
            return {"severity": "P1", "category": "critical"}

        elif any(word in res for word in ["p2", "warning", "suspicious"]):
            return {"severity": "P2", "category": "warning"}

        else:
            return {"severity": "P3", "category": "normal"}
'''
import requests
from app.config import settings

class ClassificationAgent:
    def classify(self, text):
        prompt = f"""
        Classify the following into:
        severity: P1/P2/P3/P4
        category: safety/illegal/system/normal

        Text: {text}

        Return JSON.
        """

        res = requests.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={"model": settings.OLLAMA_MODEL, "prompt": prompt, "stream": False},
        ).json()["response"]

        if "P1" in res:
            return {"severity": "P1", "category": "critical"}
        elif "P2" in res:
            return {"severity": "P2", "category": "warning"}
        return {"severity": "P3", "category": "normal"}
'''
