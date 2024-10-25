import os
import aiosmtplib

from dotenv import load_dotenv
from email.message import EmailMessage

async def send_emails_to_prospect_and_attorney(lead):

    load_dotenv()
    
    # Note: Currently implemented using SMTP. However, in production use, would leverage email service like Amazon SES, etc. for reliability and scalability.    
    smtp_hostname = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    print(smtp_username, smtp_password)

    prospect_message = EmailMessage()
    prospect_message["From"] = smtp_username
    prospect_message["To"] = lead.email
    prospect_message["Subject"] = "Thank you for your submission"
    prospect_message.set_content(f"Dear {lead.first_name} {lead.last_name},\n\nThank you for submitting your information.\n\nBest regards,\nCompany")
    print(prospect_message.get_content())
    # TODO: Attorney email functionality is not implemented yet.
    # Reason: Requirement for obtaining the attorney's email was unclear.
    # Note: This can be implemented similarly to how we send an email to a prospect once the requirements are clarified.

    try:
        await aiosmtplib.send(prospect_message, hostname=smtp_hostname, port=smtp_port, username=smtp_username, password=smtp_password, start_tls=True)
        print("Emails sent successfully.")
    except Exception as e:
        print(f"Failed to send emails: {e}")

