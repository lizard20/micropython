from machine import Pin, PWM

'''
    Produce a PWM signal output 
    in Port 15
'''

PORT = 15
FREQUENCY = 10_000 # Hz
DUTY_CYCLE = 512 # 1023 - 100 %

pwm = PWM(Pin(PORT), freq = FREQUENCY, duty = DUTY_CYCLE)

print(f"Frequency:  {FREQUENCY:,} Hz")
print(f"Duty Cycle: {DUTY_CYCLE*100/1023 :.2f} % ")

