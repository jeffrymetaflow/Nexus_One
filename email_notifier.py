import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")

def send_notification_email(record):
    subject = f"New Nexus One Client Intake: {record['Business Name']}"
    content = f"""
    A new client intake form has been submitted.

    Business Name: {record['Business Name']}
    Contact: {record['Contact Name']}
    Email: {record['Email']}
    Phone: {record['Phone']}
    Industry: {record['Industry']}
    Number of Users: {record['Number of Users']}
    Domain: {record['Domain']}
    Needs: {record['Needs']}
    """

    message = Mail(
        from_email=EMAIL_FROM,
        to_emails=EMAIL_TO,
        subject=subject,
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"Error sending email: {e}")
        return None

def send_thank_you_email(record):
    subject = "Thanks for contacting Nexus One Technologies!"
    content = f"""
    Hi {record['Contact Name']},

    Thank you for submitting your information to Nexus One Technologies. We're excited to learn more about your business, {record['Business Name']}.

    One of our team members will review your needs and follow up shortly.

    — The Nexus One Technologies Team
    """

    message = Mail(
        from_email=EMAIL_FROM,
        to_emails=record['Email'],
        subject=subject,
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"Error sending thank you email: {e}")
        return None

