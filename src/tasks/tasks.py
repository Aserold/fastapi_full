import smtplib
from email.message import EmailMessage

from celery import Celery
from src.config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6378')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Hello World!'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        'div'
        f'<h1>Hello World!</h1>'
        f"<p>What's good {username}?"
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
