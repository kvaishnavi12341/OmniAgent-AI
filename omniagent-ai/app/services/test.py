from app.services.email_service import EmailService

EmailService().send_email(
    subject="TEST",
    body="Hello from OmniAgent"
)