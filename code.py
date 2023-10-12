import time
import default

from steps import first as first_sequence
from steps import second as second_sequence
from steps import third as third_sequence

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
wait_time = default.wait_time

first_section = first_sequence.first(motor1, motor2, sonar, speed, turn_speed, slow_speed, wait_time)
second_section = second_sequence.second(motor1, motor2, sonar, speed, turn_speed, slow_speed, wait_time)
third_section = third_sequence.third(motor1, motor2, sonar, speed, turn_speed, slow_speed, wait_time)

first_section.run()

second_section.run()

third_section.run()