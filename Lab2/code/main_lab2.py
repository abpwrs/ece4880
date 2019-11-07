#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta
from time import sleep
import serial

# Twilio Texting
from TwilioCreds import TwilioCreds
from twilio.rest import Client

def main():
    ser = serial.Serial()
    ser.baudrate = 9600
    #ser.port = 'COM7'
    ser.port = '/dev/cu.usbmodem14201'
    ser.open()
    sleep(3) # required when opening port
    delta = timedelta(seconds=3)
    time_can_send_again = datetime.now() + delta

    print('Waiting for texts')
    while(True):
        # sleep(.3)
        if "sendtext" in str(ser.readline()) and datetime.now() > time_can_send_again :
            sendText()
            time_can_send_again = datetime.now() + delta
            print('SENDING THE TEXT')

def sendText():
    print('sending text!')
    client = Client(TwilioCreds().sid(), TwilioCreds().auth_token())
    hours = datetime.now().hour
    minutes = datetime.now().minute
    if minutes < 10:
        minutes = f'0{minutes}'

    msg = f"Critical saftey event at {hours}:{minutes}"

    try:
        message = client.messages.create(
            body=msg,
            from_='+12054984327',
            to='+15157834876'
            )
        print(message.sid)

    except Exception as e:
        print('error:')


if __name__ == "__main__":
    main()
