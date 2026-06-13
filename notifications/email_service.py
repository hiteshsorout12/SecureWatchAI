import os
import smtplib
import threading

from email.message import EmailMessage
import traceback
from dotenv import load_dotenv

load_dotenv()


def send_email_alert(
        subject,
        body,
        attachment_path=None):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("ALERT_RECEIVER")

    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content(body)

    if attachment_path:

        with open(
            attachment_path,
            "rb"
        ) as file:

            file_data = file.read()
            file_name = os.path.basename(
                attachment_path
            )

        msg.add_attachment(
            file_data,
            maintype="image",
            subtype="jpeg",
            filename=file_name
        )

    try:

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            timeout=15
        ) as smtp:

            smtp.login(
                sender,
                password
            )

            smtp.send_message(msg)

        print("✅ Email Sent Successfully")

        return True

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"❌ Email Failed: {type(e).__name__}: {e}")
        return False


def send_email_async(
        subject,
        body,
        attachment_path=None):

    thread = threading.Thread(
        target=send_email_alert,
        kwargs={
            "subject": subject,
            "body": body,
            "attachment_path": attachment_path
        }
    )

    thread.start()

    return thread