from server import mcp
from utils.send_proton import send_proton_mail
from utils.send_gmail import send_gmail_mail

@mcp.tool()
def send_via_proton(to, subject, body):
    """
    A tool to send an email via Proton Mail
    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    return send_proton_mail(to, subject, body)

@mcp.tool()
def send_via_gmail(to, subject, body):
    """
    A tool to send an email via Gmail
    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    return send_gmail_mail(to, subject, body)