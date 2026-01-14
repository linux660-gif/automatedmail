import smtplib
from email.message import EmailMessage
import os

class EmailAPI:
    def __init__(self):
        path = None
    def  send_email_with_attachment(self, file_path:str):
        sender_email = os.getenv("EMAIL_USER")
        receiver = os.getenv("EMAIL_PASS")

        message_object = EmailMessage()
        message_object['Subject'] = 'Update on Registration'
        message_object['To'] = receiver
        message_object['From'] = sender_email 
        message_object.set_content('Here is a new upload in registration attached ')

        with open(file_path,'rb') as file:
            file_data = file.read()
            file_name = file.name


        message_object.add_attachment(
            file_data,
            maintype = 'application',
            subtype = 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            filename = file_name

        )

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(sender_email, 'nymq netk fodr psta ')
        server.send_message(message_object)


