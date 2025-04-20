from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import os
import smtplib
import ssl

if os.path.isfile('env.py'):
    import env

g_username = os.environ["g_username"]
g_password = os.environ["g_password"]

def send_gmail_mail(to, subject, body):
    """
    Send an email using Gmail.
    
    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """

    host = "smtp.gmail.com"
    port = 587

    message = MIMEMultipart()
    message.attach(MIMEText(body, 'html'))
    message["Subject"] = subject
    message["From"] = g_username
    message['To'] = to

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    response = {"response": ""}
    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(g_username, g_password)
        print("Logged in")
        try:
            server.sendmail(
                g_username, to, message.as_string())
            response["response"] = f"Email sent to {to} with subject '{subject}'"
        except smtplib.SMTPException as e:
            response["response"] = f"ERROR! {e}"

    return json.dumps(response)
