import yagmail
import os
import time
from datetime import datetime as dt


sender = "aravind.merugu2610@gmail.com"
receiver = "aravindmeruguwgl@gmail.com"
subject = "EveryDay Mail"
contents = """
sending mail to multiple users.
"""
while(True):
  now = dt.now()
  if now.hour == 10 and now.minute == 25:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver,subject=subject,contents=contents)
    print('Email Sent')
    time.sleep(60.0)