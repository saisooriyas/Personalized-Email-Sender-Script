import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read CSV file
with open('Book1.csv', 'r') as file:
    reader = csv.DictReader(file)
    recipients = list(reader)

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port =587
smtp_username = 'saisooriya2003@gmail.com'
smtp_password = 'wstr hkoe lbxt kdww'
sender_email = 'saisooriya2003@gmail.com'
subject = 'Personalized Email'

# Email template
email_template = """
Hello Krishna,

Thank you for being a valued customer at {company}. We appreciate your business.

Best regards,
Your Company
"""

# Connect to SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Send personalized emails
    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "saisooriyait@smvec.ac.in"
        msg['Subject'] = subject

        # Personalize email content
        body = email_template.format(**recipient)
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, "saisooriyait@smvec.ac.in", msg.as_string())

print("Emails sent successfully.")
