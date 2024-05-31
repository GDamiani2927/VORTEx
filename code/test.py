#type: ignore
import board
import time
from adafruit_motor import motor
import pwmio
import digitalio
import analogio

pwmA = pwmio.PWMOut(board.GP14, frequency=50)
pwmB = pwmio.PWMOut(board.GP15, frequency=50)
motor1 = motor.DCMotor(pwmA,pwmB)

ch1 = digitalio.DigitalInOut(board.GP11)
ch2 = digitalio.DigitalInOut(board.GP12)
rot = 0
old1 = ch1.value
old2 = ch2.value

while True:
    motor1.throttle = .5

    if ((ch1.value != old1) or (ch2.value != old2)):
        rot += 1
    print(rot/28)
    old1 = ch1.value
    old2 = ch2.value

    #print("ch1:")
    #print(ch1.value)
    #print("ch2:")
    #print(ch2.value)
