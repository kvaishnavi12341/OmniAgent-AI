from app.services.ticket_service import TicketService
from app.services.alert_service import AlertService

class IncidentAgent:
    def __init__(self):
        self.ticket_service = TicketService()
        self.alert_service = AlertService()

    def handle(self, text, classification):
        ticket = self.ticket_service.create_ticket({
            "text": text,
            "severity": classification["severity"]
        })

        if classification["severity"] == "P1":
            self.alert_service.send_alert(text)

        return ticket