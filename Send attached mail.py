import yagmail
import os

sender = "aravind.merugu2610@gmail.com"
receiver = "aravind.merugu2610@gmail.com"
subject = "Hi, Aravind"
contents = ["""
😃😃😃😃
""",'contacts.csv']

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=contents)
print('Email Sent')
