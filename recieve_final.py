
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import numpy as np
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

#setup radio
radio = NRF24(GPIO, spidev.SpiDev())
#Gpio 8 i.e Csn pin
radio.begin(0, 17)
radio.setPayloadSize(32) # PayloadSize is 32 bytes
radio.setChannel(0x76) # Any channel can be used
radio.setDataRate(NRF24.BR_1MBPS)# Slower data rate the better range
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()
#Now code starts to listen from arduino.

def position():
    while True:
        while not radio.available(0): # This while loop checks if there is any message recieved.
            #time.sleep(1/100)
	    print("Nothing")

        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
    
        string = ""
        #This loop iterates over the received message and saves it in a string for display.
        for n in receivedMessage:
            if (n >= 32 and n <= 126):
                string += chr(n)
            
        split_string = string.split(" ")
        split_string = filter(lambda name: name.strip(), split_string)
        print(split_string)
        if(float(split_string[2]) >= 8.0):
            print("****************** LIGHT ON ***********************")
	    time.sleep(2)
	    GPIO.output(20, GPIO.LOW)
	    print("****************** IT'S TURNED ON *****************")
	    time.sleep(3)
	    gather()
	elif(float(split_string[2]) <= -8.0):
            print("****************** LIGHT OFF **********************")
            time.sleep(2)
            GPIO.output(20, GPIO.HIGH)
            print("****************** IT'S TURNED OFF *****************")
            time.sleep(3)
            gather()
        time.sleep(.1)


def startup():
    while True:
        while not radio.available(0): # This while loop checks if there is any message recieved.
            time.sleep(1/100)

        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
    
        string = ""
        #This loop iterates over the received message and saves it in a string for display.
        for n in receivedMessage:
            if (n >= 32 and n <= 126):
                string += chr(n)
    
        split_string = string.split(" ")
        split_string = filter(lambda name: name.strip(), split_string)
        #print(split_string)
        if (float(split_string[0]) <= 0.0):
            print("*************** POSITION YOUR HAND *******************")
            position()
        time.sleep(.1)


def gather():
    while True:
        #print("***********************INITIATE THE OPERATION*****************")
        while not radio.available(0): # This while loop checks if there is any message recieved.
            time.sleep(1/100)

        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
    
        string = ""
            #This loop iterates over the received message and saves it in a string for display.
        for n in receivedMessage:
            if (n >= 32 and n <= 126):
                string += chr(n)
            
            #print("Three axis values: {} ".format(string))
        split_string = string.split(" ")
        split_string = filter(lambda name: name.strip(), split_string)
            #print(split_string)
            #print split_string[0], split_string[1], split_string[2]
        
        print(split_string)
        
        if (float(split_string[0]) >= 10.00):
            print("************* Do the Gesture **************")
            startup()

        time.sleep(.1)

gather()

    


        
