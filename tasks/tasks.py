import smtplib
from email.message import EmailMessage
from celery import Celery
celery = Celery('tasks', broker='redis://localhost:6379')

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER="***********************"
SMTP_PASSWORD="****************"


def send_email():
    email = EmailMessage()
    email['Subject'] = 'Приветики'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1>Вам телеграмма от гиппопотама!</h1>'
        '</div>',
        subtype='html'
    )
    return email

@celery.task
def send_email_report():
    email = send_email()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)