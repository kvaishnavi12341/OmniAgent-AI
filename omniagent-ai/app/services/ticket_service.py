import json

class TicketService:
    def create_ticket(self, data):
        with open("data/tickets.json", "a") as f:
            f.write(json.dumps(data) + "\n")
            
        return data