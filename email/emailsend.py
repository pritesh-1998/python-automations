import smtplib
import os

email_address = os.environ.get("email")
email_password = os.environ.get("emailpass")
# print(email, password)

# email_address="";
# email_password="";

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies ourselves with the mail servers
    smtp.starttls()  # start TLS
    smtp.ehlo()  # reidentify ourselves as an encrypted connection
    smtp.login(email_address, email_password)  # authenticate login
    subject = "first email sent"
    body = "Hello this is my first email sent"
    msg = f'Subject: {subject}\n\n{body}\n'
    smtp.sendmail(email_address, 'pritesh.l@somaiya.edu', msg)
    print("Email Sent")
