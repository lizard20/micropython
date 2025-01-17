from machine import Pin
from time import sleep

'''
    Blink a Led connected to port GPIO2
'''

PORT = 2       # GPIO2
SECONDS = 0.5

led = Pin(PORT,     # port number
          Pin.OUT)  # port configured as output

while(True):
    led.on()
    sleep(SECONDS)
    led.off()
    sleep(SECONDS)
    print(f"Blinking on Port GPIO{PORT}")





