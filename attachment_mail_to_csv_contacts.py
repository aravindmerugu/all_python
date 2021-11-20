import yagmail
import os
import pandas


sender = "aravind.merugu2610@gmail.com"
subject = "attachment mail to csv contacts"

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')
for index, row in df.iterrows():
  contents = [f"""
Hey, {row['name']} you have to pay {row['amount']}
Bill is attached
""",row['filepath']]
  yag.send(to=row['email'],subject=subject,contents=contents)
  print('Email Sent')