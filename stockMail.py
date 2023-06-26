import os
import ssl 
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr 


email_adress = os.environ.get('email_user')
email_password = os.environ.get('email.pass')
email_receiver = 'jiteser600@edulena.com'

em = EmailMessage()
yf.pdr_override()                         
start = dt.datetime(2018,12,1)
now = dt.datetime.now()

stock = 'AMZN'
TargetPrice = 120

em['Subject'] = 'Alert on ' + stock
em['From'] = email_adress
em['To'] = email_receiver
context = ssl.create_default_context()

alerted = False

while 1:
    
    df = pdr.get_data_yahoo(stock, start, now)
    currentClose = df['Adj Close'][-1]

    condition = currentClose > TargetPrice

    if (condition and alerted == False):
        alerted = True
        message = stock  + ' has activated the alert price of ' + str(TargetPrice) + '\nCurrent Price: ' + str(currentClose)

        em.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(email_adress, email_password)
            smtp.send_message(em)

            print('Completed')

    else: 
        print("No New Alerts")

    time.sleep(180)