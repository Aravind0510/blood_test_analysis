import os
import smtplib
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename

def save_pdf(pdf_file):
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    # Define the file path
    filepath = os.path.join('uploads', pdf_file.filename)

    # Save the PDF file
    pdf_file.save(filepath)
    return filepath

def send_email(to_email, subject, content):
    sender_email = "aravindhan051000@gmail.com"
    password = "gbjx lknz dnxr gxtz"

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())
