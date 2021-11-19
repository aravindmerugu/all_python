import yagmail
import os
import time

while(True):
  sender = "aravind.merugu2610@gmail.com"
  receiver = "aravindmeruguwgl@gmail.com"
  subject = "Periodic Mail"
  contents = """
  sending mail to multiple users.
  """

  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject,contents=contents)
  print('Email Sent')
  time.sleep(60.0)