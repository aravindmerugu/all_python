import yagmail
import os

sender = "aravind.merugu2610@gmail.com"
receiver = "aravindmeruguwgl@gmail.com"
subject = "Script Mail"
contents = """
This is a mail sent by running a python script.
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=contents)
print('Email Sent')