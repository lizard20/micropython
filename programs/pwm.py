from machine import Pin, PWM

'''
    Produce a PWM signal output 
    on Port GPIO15

    Author: Aldo Núñez
'''

PORT = 15   # GPIO15
FREQUENCY = 10_000  # Hz
DUTY_CYCLE = 512    # 1023 - 100 %

pwm = PWM(Pin(PORT),            # port number
          freq = FREQUENCY,     # frequency
          duty = DUTY_CYCLE)    # duty cycle

print(f"PWM output on Port: GPIO{PORT}")
print(f"Frequency:  {pwm.freq():,} Hz")
print(f"Frequency:  {pwm.duty()*100/1023:0.2f} %")
