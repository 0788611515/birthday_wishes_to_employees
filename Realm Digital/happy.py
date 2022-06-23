#import the libraries

import datetime
import pandas as pd
import numpy as np
import smtplib
import ssl
from email.mine.text import MIMEText as MT
from email.mine.multipart import MIMEMultipart as MM

#load the birthday list data
from Api import files
files.array()

# Read in the data
df = pdl.read_array('https://interview-assessment-1.realmdigital.co.za/employees')

#show data
df = 'https://interview-assessment-1.realmdigital.co.za/'
#create a  function to send email
def email_func(subject, birthday_receiver, name):

#Store teh email address for the receiver, and also for the sender note that we need to store the senders email password
birthday_receiver = 'employee_email'
sender = 'company_email'
sender_password = 'Admin_Password'

#Create a MIMEMultipart object
msg = MM()
msg['Subject'] = subject+''+str(name)+'!'

#create the HTML text of wishlist
HTML = """
<html>
  <body>
    <h1>Happy Birthday</h1>
     <img src="https://img.ltwebstatic.com/images3_pi/2021/07/21/1626834910a245b928b36fac41a07b524b38d1afec_thumbnail_600x.webp" 
     alt = "img" width= "650" height="370"></img>
     <p>photo take by Sensei Alex Sylvain </p>
     <h2>
       <p>Bonjour! <br>
       I wish you a wonderful day on this special moment of the year
       from;<br>
       Your Best company
       </p>
     </h2>
  </body>
</html>

"""
#Here we will create a HTML MIMEText object
MTObj = MT(HTML, "html")

#attach the MIMEText object into the message container
msg.attach(MTObj)

#Create a secure connection with the server and the email
#create the secure socket layer(SSL) context object
SSL_context = ssl.create_default_context()

#Create the secure simple Mail transfer protocol (MSTP) connection
server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context= SSl_context)

#login to email account
server.login(sender_email, sender_password)

#send the Email
server.sendmail(sender_email, receiver_email, msg.as_string())

#get todays date
today = datetime.date.today()

#get the current year
year = today.year
#loop through the birthday list in the API to send email to employee
for i in range(0, len(df)):

    #get the employee month
    month = df['dateOfBirth'][i]
    #get the employee day of birthday
    day = df['dateOfBirth'][i]
    #get the employee name
    name = df['name'][i]
    #get the employee lastname
    lastname = df['lastname'][i]
    #get wish employmentStartDate
    work_anniversary = df['employmentStartDate'][i]
    #get employee email address
    email = df['receiver_email'][i]

    #get the employee birthday
    birthday = datetime.date(year, month, day)

    #now let's check if today is the employee's birthday
    if birthday == today:
        email_func('Happy Birthday', email, name, lastname)
        print('send happy birthday')
    else:
        print('No one is celebrating today')




