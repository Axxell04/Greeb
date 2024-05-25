import smtplib
from email.mime.text import MIMEText
import dotenv
import os

dotenv.load_dotenv()

sender_mail = os.getenv("SENDER_MAIL")
password = os.getenv("SENDER_PASS")
receiver_mail = os.getenv("RECEIVER_MAIL")
message = "Subject: Consulta\n\nPrueba Numero 5"

def send_mail(message="", contact_mail=""):
    msg = MIMEText(message)
    msg["Subject"] = contact_mail
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg["Charset"] = "UTF-8"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_mail, password)
        server.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=msg.as_string())
    