from machine import ADC, Pin
from time import sleep

'''
    Read analog input on PORT GPIO34

    Author: Aldo Núñez
'''

PORT = 34   # GPIO34
TIME = 1    # second

RESOLUTION = 2**12    # 12 bits of resolution, 0-4095
MAX_VOLTAGE = 3.3     # Volts
CONVERSION =  MAX_VOLTAGE/RESOLUTION

port = Pin(PORT)
adc = ADC(port)

while True:
    adc_value = adc.read()              # read  an integer between: 0–4095
    voltage = adc_value * CONVERSION    # convert the integer value to voltage  
    print(f"Analog input on Port: GPIO{PORT}, adc value: {adc_value}, voltage: {voltage:.2f}v")
    sleep(TIME)

