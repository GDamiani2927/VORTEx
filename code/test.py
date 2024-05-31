#type: ignore
import board
import time
from adafruit_motor import motor
import pwmio
import digitalio

pwmA = pwmio.PWMOut(board.GP14)
pwmB = pwmio.PWMOut(board.GP15)
motor1 = motor.DCMotor(pwmA,pwmB)

ch1 = digitalio.DigitalInOut(board.GP0)
ch2 = digitalio.DigitalInOut(board.GP1)
ticks = 0
old1 = ch1.value

while True:
    motor1.throttle = 1
    if (ch1.value == False and old1 == True):
        ticks += 1
    old1 = ch1.value
    print("rots:")
    print(ticks/54)
