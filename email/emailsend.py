import smtplib
import os

email_address = os.environ.get("email")
email_password = os.environ.get("emailpass")
# print(email, password)

# email_address="";
# email_password="";

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # if you using local server for testing
    # with smtplib.SMTP_SSL('localhost', 1025) as smtp:

    # all these 4 lines will be commented if you are using local server and smtp_ssl
    # smtp.ehlo()  # identifies ourselves with the mail servers
    # smtp.starttls()  # start TLS
    # smtp.ehlo()  # reidentify ourselves as an encrypted connection
    smtp.login(email_address, email_password)  # authenticate login

    subject = "first email sent"
    body = "Hello this is my first email sent"

    msg = f'Subject: {subject}\n\n{body}\n'

    # python -m smtpd -c DebuggingServer -n localhost:1025
    # you can also use local server for testing run above command in terminal or cmd

    smtp.sendmail(email_address, 'pritesh.l@somaiya.edu', msg)
    print("Email Sent")
