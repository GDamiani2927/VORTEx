#type: ignore
import board
import time
from adafruit_motor import motor #motor library
import pwmio #PWM pins library
import digitalio #digital input/output library

pwmA = pwmio.PWMOut(board.GP14) #motor PWM pin A declaration
pwmB = pwmio.PWMOut(board.GP15) #motor PWM pin B declaration
motor1 = motor.DCMotor(pwmA,pwmB) #motor declaration

ch1 = digitalio.DigitalInOut(board.GP0) #encoder channel 1 input declaration
ch2 = digitalio.DigitalInOut(board.GP1) #encoder channel 1 input declaration
ticks = 0 #number of encoder value changes
old1 = ch1.value #stores old endcoder values

while True: #find number of rotations
    motor1.throttle = 1 #sets motor to full speed
    if (ch1.value == False and old1 == True): #if encoder values change False --> True
        ticks += 1
    old1 = ch1.value #store old encoder value
    print("rots:") 
    print(ticks/54) #find rotations using gearbox and encoder ratio
