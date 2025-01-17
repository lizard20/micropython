from machine import Pin
from time import sleep

'''
    Read  port GPIO13 every 1 second
'''

PORT = 13    # GPIO13
SECONDS = 1

read_port = Pin(PORT,           # port number
                Pin.IN,         # port configured as input
                Pin.PULL_UP)    # the port starts  HIGH

while True:
    input_port = read_port.value()
    print(f"Input on pin {PORT}: {input_port}")
    sleep(SECONDS)
