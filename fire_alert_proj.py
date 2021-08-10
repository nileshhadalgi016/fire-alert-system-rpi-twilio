import RPi.GPIO as GPIO
import time
import os
from twilio.rest import Client 

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

account_sid =  "enter your account SID here"
auth_token =   "enter your account AUTH TOKEN here"

client = Client(account_sid, auth_token)

# Note : Change xxxx with your phone number


message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='flame sensor started ',
                              to='whatsapp:+91xxxxxxxxxx'
                          )

def callback(channel):
    print("Flame Detected")
    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='http://maps.google.com/maps?q=24.197611,120.780512',
                              to='whatsapp:+91xxxxxxxxxx'
                          )
    time.sleep(60*60)

GPIO.add_event_detect(channel,GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)

