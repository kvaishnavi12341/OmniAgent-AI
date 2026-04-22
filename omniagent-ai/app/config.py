import os
from dotenv import load_dotenv

#load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

class Settings:
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    EMAIL_TO = os.getenv("EMAIL_TO")
    RBAC_ROLE=os.getenv("RBAC_ROLE","user")

    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

settings = Settings()