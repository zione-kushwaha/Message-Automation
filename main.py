'''
# Twilio 
# datetime module
# time
'''
# setup 
'''
1. twilio client setup
2. user inputs
3 scheduling logic
4. send message
'''

from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# twilio client setup
# Load credentials from environment variables for security
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

if not account_sid or not auth_token or not whatsapp_number:
    print("Error: Missing Twilio credentials. Please check your .env file.")
    print("Make sure you have:")
    print("- TWILIO_ACCOUNT_SID")
    print("- TWILIO_AUTH_TOKEN") 
    print("- TWILIO_WHATSAPP_NUMBER")
    exit(1)

client = Client(account_sid, auth_token)


# send message function

def send_whatsapp_message(to, message):
    try:
        sent_message = client.messages.create(
            from_=whatsapp_number,
            body=message,
            to=f'whatsapp:{to}'
        )
        print(f"Message sent successfully: {sent_message.sid}")
        print(f"Message status: {sent_message.status}")
        print(f"To: {sent_message.to}")
        print(f"From: {sent_message.from_}")
        
        # Check message status after a short delay
        time.sleep(2)
        updated_message = client.messages(sent_message.sid).fetch()
        print(f"Updated status: {updated_message.status}")
        if updated_message.error_code:
            print(f"Error code: {updated_message.error_code}")
            print(f"Error message: {updated_message.error_message}")
            
    except Exception as e:
        print(f"Error sending message: {e}")


# setup the user input 

name = input("Enter your name: ")
recipient_number = input("Enter your WhatsApp number (in E.164 format, e.g., +9779807151008): ")
message = input("Enter the message you want to send: ")


# parse the date/time and calculate the delay
date_str = input("Enter the date (YYYY-MM-DD): ") # 2024-12-01
time_str = input("Enter the time (HH:MM): ") # 15:00


# combine date and time into a single datetime object
scheduled_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

# current time
current_time = datetime.now()

# calculate the delay in seconds
delay = (scheduled_time - current_time).total_seconds()

# check if the delay is positive
if delay < 0:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    print(f"Message will be sent in {delay} seconds.")

    time.sleep(delay)  # wait for the specified delay

    send_whatsapp_message(recipient_number, message)
