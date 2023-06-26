# StockPriceAlert
Automated Email Notification for Stock Price Surpassing Investment Amount using Python


<h3> Creating an automated email sender using Python. </h3>

* The script is designed to send an email notification whenever the stock price surpasses the invested amount. The code utilizes the Python programming language to achieve this functionality.

  This code creates a program that periodically checks the stock price and sends an email notification when the price surpasses the specified target, allowing for timely monitoring of stock investments.

1. The necessary libraries such as os, ssl, smtplib, imghdr, EmailMessage, yfinance, datetime, pandas, and time are imported.
2. Email-related variables, such as the sender's email address, password, and receiver's email address, are initialized.
3. The target stock symbol and price are defined.
4. An EmailMessage object is created and initialized with subject, sender, receiver, and content. The SSL context for secure email communication is established.
5. A while loop continuously fetches the latest stock data from Yahoo Finance using the pandas_datareader library.
The current stock price is compared with the target price, and if the condition is met and an alert hasn't been sent before, an email is sent with the relevant information.
The email is sent using the Gmail SMTP server.
6. After each check and potential email sending, the loop pauses for 180 seconds (3 minutes) using time.sleep() to avoid excessive requests.

<p align="center">
  <img width="200" alt="Screenshot 2023-06-26 at 16 58 29" src="https://github.com/adrdatta97/StockPriceAlert/assets/117360902/0ba81b69-0d2e-4adf-9e94-9d179750969b">
</p



* The code includes a temporary email address so it is left in the code. This email address will serve as the recipient for the notification emails.



