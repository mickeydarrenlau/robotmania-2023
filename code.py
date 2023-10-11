import time
import default

from steps import first as first_sequence
from steps import second as second_sequence


import board
from digitalio import DigitalInOut, Pull
button = DigitalInOut(board.GP3) # defaults to input
button.pull = Pull.DOWN # turn on internal pull-up resistor
while button.value == False:  # False == pressed
  pass

import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP27, echo_pin=board.GP26)
import board
import pwmio
from adafruit_motor import motor

PWM_M1A = board.GP8
PWM_M1B = board.GP9
PWM_M2A = board.GP10
PWM_M2B = board.GP11


# DC motor setup
M1A = pwmio.PWMOut(PWM_M1A, frequency=10000)
M1B = pwmio.PWMOut(PWM_M1B, frequency=10000)
M2A = pwmio.PWMOut(PWM_M2A, frequency=10000)
M2B = pwmio.PWMOut(PWM_M2B, frequency=10000)
motor1 = motor.DCMotor(M1A, M1B)
motor2 = motor.DCMotor(M2A, M2B)

speed = default.speed
turn_speed = default.turn_speed
slow_speed = default.slow_speed

first_section = first_sequence.first(motor1, motor2, sonar, speed, turn_speed, slow_speed)
second_section = second_sequence.second(motor1, motor2, sonar, speed, turn_speed, slow_speed)

first_section.run()


time.sleep(2)

second_section.run()

time.sleep(2)

motor2.throttle = 0.8 # section 3
time.sleep(0.8)
motor2.throttle = 0.0

time.sleep(2)

motor1.throttle = 0.8 
motor2.throttle = 0.8

time.sleep(2)

while sonar.distance > 14:
    time.sleep(0.1)
    pass



motor1.throttle = 0.0
motor2.throttle = 0.0

time.sleep(2)

motor1.throttle = 0.8
time.sleep(0.8)
motor1.throttle = 0.0

time.sleep(2)

motor1.throttle = 0.8
motor2.throttle = 0.8

time.sleep(2)

while sonar.distance > 14:
    time.sleep(0.1)
    pass

motor1.throttle = 0.0
motor2.throttle = 0.0

time.sleep(2)

motor1.throttle = 0.8
time.sleep(0.8)
motor1.throttle = 0.0

