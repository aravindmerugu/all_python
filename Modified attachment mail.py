import yagmail
import os
import pandas


sender = "aravind.merugu2610@gmail.com"
subject = "Modified attachment mail to csv contacts"

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

df = pandas.read_csv('contacts.csv')

def generate_file(filename, content):
  with open(filename, 'w') as file:
    file.write(content)

for index, row in df.iterrows():
  name = row['name']
  filename = name + ".txt"
  amount = str(row['amount'])
  receiver_email = row['email']
  generate_file(filename,amount)
  contents = [f"""
Hey, {name} you have to pay {amount}
Bill is attached
""",filename]
  yag.send(to=receiver_email,subject=subject,contents=contents)
  print('Email Sent')