# Dependancy inversion ( SOLID -> D)
# This ensures that low level(parent) class must not dependent of high(child) level class


# It violates the single dependency ('S'OLID) as the notification is using to send email.Notification must serve a single task
class EmailService:
    def send(self, message):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self):
        self.service = EmailService()

    def notify(self, message):
        self.service.send(message)