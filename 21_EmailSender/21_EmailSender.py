import smtplib, ssl
port = 456
sender = "Your Email"
password = "Your Password"

recieve = "Reciever's Mail ID"

message = """\
Subject: Sent via Python

Hello world Jarvis in making
"""
context = ssl.create_default_context()

print("Sending process initiated")
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(sender,password)
    server.sendmail(sender,recieve,message)

print("Mail sent Successfully")
