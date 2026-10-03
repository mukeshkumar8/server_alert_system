import smtplib
from email.message import EmailMessage


def send_email_alert(alert_message):

    sender_email = "mukesh.kumarbizzdose@gmail.com"
    receiver_email = "mk9695@gmail.com"
    app_password = "Mukeesh@1234567"

    message = EmailMessage()

    message["Subject"] = "SERVER ALERT"
    message["From"] = sender_email
    message["To"] = receiver_email

    message.set_content(
        f"""
Server Alert Detected

Alert:
{alert_message}

Please check the server.
"""
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)

    print("Email alert sent successfully!")


send_email_alert("Memory usage is above 80%")