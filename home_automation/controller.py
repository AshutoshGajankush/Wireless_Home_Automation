# Python code for controller native service -
# smart sensing - controller.py

import RPi.GPIO as GPIO
import time
import sys
import requests

GPIO.setmode(GPIO.BCM)
#ROOM_SENSOR_PIN = 27
#LIGHT_SENSOR_PIN = 20
#GPIO.setup(ROOM_SENSOR_PIN, GPIO.IN)
GPIO.setup(20, GPIO.IN)
"""
def readingRoomSensor():
    if GPIO.input(ROOM_SENSOR_PIN):
        print 'motion detected'
        return 1
    else:
        return 0
"""
def readingLightSensor():
    if GPIO.input(20):
        print 'light OFF'
        return 1
    else:
        print 'light ON'
        return 0

def runController():
    """
    roomState = readingRoomSensor()
    if roomState == 1:
        setRoomState('yes')
    else:
        setRoomState('no')
    """
    lightstate = readingLightSensor()
    if lightstate == 1:
        setLightState('OFF')
    else:
        setLightState('ON')
"""
def setRoomState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/room/1/', data=values, auth=('pi', 'group5iot'))
""" 
def setLightState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/light/1/', data=values, auth=('pi', 'group5iot'))

while True:
    try:
        runController()
        #time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
