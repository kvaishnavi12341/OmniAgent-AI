import requests
from app.config import settings

class AlertService:
    def send_alert(self, msg):
        requests.post(settings.SLACK_WEBHOOK_URL, json={"text": msg})