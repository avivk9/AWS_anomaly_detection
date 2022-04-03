import boto3
import smtplib, ssl

smtp_server = "stmp.gmail.com"
port = 465
sender_email ='awsomeanomalydetector@gmail.com'
receiver_email = ["avivkeinan1@gmail.com"]
password = "SheerTheQueen22"
context = ssl.create_default_context()
message = "There is no Activity on the server. We are shtting it down."
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)