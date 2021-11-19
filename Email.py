import yagmail
import os

sender = "aravind.merugu2610@gmail.com"
receiver = ["vashistsunny56@gmail.com","aravindmeruguwgl@gmail.com"]
subject = "Script Mail"
contents = """
sending mail to multiple users.
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=contents)
print('Email Sent')