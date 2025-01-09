from machine import Pin
from time import sleep

'''
    Read  port 2 of the esp32 
    microcontroller every 1 second
'''

PORT = 2
SECONDS = 1

read_port = Pin(PORT, Pin.IN, Pin.PULL_UP)

while True:
    input_port = read_port.value()
    print(f"Input on pin {PORT}: {input_port}")
    sleep(SECONDS)
