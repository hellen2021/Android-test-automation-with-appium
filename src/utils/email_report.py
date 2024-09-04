import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_report(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_password, attachment_path):
    # Create a multipart message
    msg = MIMEMultipart()

    # Email sender, receiver, and subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Open the report file in binary mode
    filename = os.path.basename(attachment_path)
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    # Encode the attachment in base64
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')

    # Attach the file to the email
    msg.attach(part)

    # Set up the server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(from_email, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email} successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Example usage:
if __name__ == "__main__":
    send_email_report(
        subject="Consumer UAT Test Report",
        body="Please find the attached test report.",
        to_email="elleville23@gmail.com",
        from_email="hellencheptoo19@gmail.com",
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        smtp_password="hcea cbul whqk rwoj",
        attachment_path="/Users/hellen.cheptoo/PycharmProjects/src/report.html"
    )
