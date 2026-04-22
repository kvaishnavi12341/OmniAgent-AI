from app.agents.conversation_agent import ConversationAgent
from app.agents.classification_agent import ClassificationAgent
from app.agents.incident_agent import IncidentAgent
from app.agents.escalation_agent import EscalationAgent
from app.agents.automation_agent import AutomationAgent
from app.utils.rbac import RBAC
from app.utils.logger import Logger
from app.utils.metrics import Metrics

class Orchestrator:
    def __init__(self):
        self.conv = ConversationAgent()
        self.cls = ClassificationAgent()
        self.incident = IncidentAgent()
        self.escalation = EscalationAgent()
        self.auto = AutomationAgent()
        self.rbac = RBAC()
        self.logger = Logger()

        #if not self.rbac.check_access("write"):
         #   return {"error": "Access denied"}

    def process(self, text):
        response = self.conv.respond(text)

        classification = self.cls.classify(text) or {}
        #Metrics.track(classification["severity"])
        severity = classification.get("severity", "low")

        Metrics.track(severity)

        ticket = self.incident.handle(text, classification)

        self.escalation.handle(ticket)

        automation = self.auto.run(classification)

        self.logger.log({
            "input": text,
            "classification": classification,
            "ticket": ticket
        })

        return {
            "response": response,
            "classification": classification,
            "ticket": ticket,
            "automation": automation
        }