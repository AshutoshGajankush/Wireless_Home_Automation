import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

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
    
    print("Three axis values: {} ".format(string))
    







        
