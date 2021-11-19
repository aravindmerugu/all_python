import yagmail
import os
import pandas


sender = "aravind.merugu2610@gmail.com"
receiver = "aravindmeruguwgl@gmail.com"
subject = "EveryDay Mail"

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')
for index, row in df.iterrows():
  contents = f"""
Hi {row['name']}
"""
  yag.send(to=row['email'],subject=subject,contents=contents)
  print('Email Sent')s