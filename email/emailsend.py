# python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib
import os
import imghdr
from email.message import EmailMessage

email_address = os.environ.get("email")
email_password = os.environ.get("emailpass")

msg = EmailMessage()
msg['Subject'] = 'first email sent'
msg['From'] = email_address
msg['To'] = 'pritesh.l@somaiya.edu'
msg.set_content('Hello this is my first email sent')

# files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
files = ['resume.pdf']

for file in files:
    # sending single image
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    # msg.add_attachment(file_data, maintype="image",
    #                    subtype=file_type, filename=file_name)
    msg.add_attachment(file_data, maintype="application",
                       subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # if you using local server for testing
    # with smtplib.SMTP_SSL('localhost', 1025) as smtp:

    smtp.login(email_address, email_password)  # authenticate login

    smtp.send_message(msg)
    print("Email Sent")
