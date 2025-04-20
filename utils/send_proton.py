import json
import os
from protonmail import ProtonMail
import env

proton = ProtonMail()

p_username = os.environ["p_username"]
p_password = os.environ["p_password"]

def send_proton_mail(to, subject, body):
    """
    Send an email using ProtonMail.
    
    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    proton.login(p_username, p_password)

    message = proton.create_message(
        recipients=[to],
        subject=subject,
        body=body
    )

    
    proton.send_message(message)

    return json.dumps({"response": f"Email sent to {to} with subject '{subject}'"})
