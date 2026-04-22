from app.services.email_service import EmailService

class EscalationAgent:
    def __init__(self):
        self.email = EmailService()

    def handle(self, ticket):
        #if ticket["severity"] == "P1":
        if ticket and ticket.get("severity") == "P1":
            self.email.send_email(
                subject="CRITICAL ALERT",
                body=str(ticket)
            )