import yagmail
import os
import time

while(True):
  sender = "aravind.merugu2610@gmail.com"
  receiver = "abhilashbommera12@gmail.com"
  subject = "Hi, Abhilash"
  contents = """
  😃😃😃😃
  """

  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject,contents=contents)
  print('Email Sent')
  time.sleep(5.0)