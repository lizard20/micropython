from machine import Pin
from time import sleep

'''
    Blink a Led connected to port 15
    of the esp32 microcontroller
'''

PORT = 15
SECONDS = 0.5

led = Pin(PORT, Pin.OUT)

while(True):
    led.on()
    sleep(SECONDS)
    led.off()
    sleep(SECONDS)
