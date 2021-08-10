# fire-alert-system-rpi-twilio   :fire:
fire alert system using flame sensor and RPI and twilio as the api for whatsapp messaging 

requirements // hardware :

- Raspberry Pi 
- Flame Sensor 
- wires 
- twilio acoount 
- smartphone with whatasapp
- RPI peripherals


## Circuite Diagram 
![F2CUGMHJAIJOMLA png](https://user-images.githubusercontent.com/57908107/128870798-08e7bdcc-ce16-48b4-a66f-aaa969ac0430.jpg)
## Pin Connections


|RPI      |    Sensor |
| ------------- | ------------- |
| 5 VCC   | 5 VCC  |
| GND | GND  |
| Pin 21  |  OUTPUT PIN  |

## code 

```

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

```

## Aboout Me <3

**NILESH HADALGI** <BR>
Instagram Page : https://instagram.com/techie_programmer <br>
YouTube : https://youtube.com/c/techieprogrammer
