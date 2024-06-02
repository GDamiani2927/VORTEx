#type: ignore
import board
import math
from adafruit_motor import motor #motor library
import pwmio #pwm pins library
import digitalio #digital input/output library
import analogio

pwmA = pwmio.PWMOut(board.GP14, frequency=50)
pwmB = pwmio.PWMOut(board.GP15, frequency=50)
motor1 = motor.DCMotor(pwmA,pwmB)

magnet = digitalio.DigitalInOut(board.GP2)
magnet.direction = digitalio.Direction.OUTPUT
magnet.value = True

button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT

ch1 = digitalio.DigitalInOut(board.GP0)
old1 = ch1.value
ticks = 0

while True:
    motor1.throttle = -1
    if(button.value):
        motor1.throttle = 0
    if (ch1.value == False and old1 == True):
        ticks += 1
    old1 = ch1.value
    rot = ticks/54
    if (rot > 75 and math.fmod(ticks, 4) == 3):
        magnet.value = False
        motor1.throttle = 0
        print("release")
        break
    print("rots:")
    print(rot)
