## MAKING EXTRA CHANGES AND ACTIONS IN EACH CASE ##

def control(status):
    if status is "empty_server":
        # closing the server
        pass
    if status is "change_server_host":
        # move to a lighter server
        pass
    if status is "hacked":
        # remove users and edit their permissions
        pass
    if status is "server_cooled_hard":
        # notify the server owner
        pass
    if status is "normal_status":
        # all good :)
        pass



















# import anomaly_detection
# import boto3
# import smtplib, ssl
#
# from boto3_basics import ec2
# smtp_server = "stmp.gmail.com"
# port = 465
# sender_email ="awsomeanomalydetector@gmail.com"
# receiver_email = "avivkeinan1@gmail.com"
# password = "SheerTheQueen22"
# context = ssl.create_default_context()
#
# class controller:
#     def __init__(self):
#         pass
#     def getStatus(self):
#         pass
#     def update(self,subject:anomaly_detection,status):
#         match status:
#             case "no activity":
#                 #instance = "i-0de58090ae091a863"
#                 #ec2.stop_instances(instance)
#                 message = "There is no Activity on the server. We are shtting it down."
#                 with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#                     server.login(sender_email, password)
#                     server.sendmail(sender_email, receiver_email, message)
#             case "hacking":
#                 iam = boto3.client('iam')
#                 for user in iam.list_users():
#                     if user['Policyname'] != "AmazonEC2FullAccess":
#                         iam.delete_user(user)
#
