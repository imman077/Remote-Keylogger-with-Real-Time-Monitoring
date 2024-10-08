import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(receiver_mail,subject,body,attachment):
    try:
        sender_email = "immanromanaj@gmail.com"
        sender_password = "lkvm mvbp xxen bjry"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_mail
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        filename = attachment
        if filename is None:
            print("Screenshot not taken, skipping email.")
            return

        with open(filename, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='png')
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
            msg.attach(attachment)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print("Screenshot E-Mail has been sent successfully!")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

        




