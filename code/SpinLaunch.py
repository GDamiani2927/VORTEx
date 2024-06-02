#type: ignore
import board
import math
from adafruit_motor import motor #motor library
import pwmio #PWM pins library
import digitalio #digital input/output library

pwmA = pwmio.PWMOut(board.GP14, frequency=50) #motor PWM pin A declaration
pwmB = pwmio.PWMOut(board.GP15, frequency=50) #motor PWM pin B declaration
motor1 = motor.DCMotor(pwmA,pwmB) #motor declaration

magnet = digitalio.DigitalInOut(board.GP2) #magnet on pin GP2
magnet.direction = digitalio.Direction.OUTPUT #magnet declaration as digital output
magnet.value = True

button = digitalio.DigitalInOut(board.GP13) #kill switch button declaration
button.direction = digitalio.Direction.INPUT

ch1 = digitalio.DigitalInOut(board.GP0) #encoder channel A declaratio as digital input
old1 = ch1.value #stores old ch1 value to check for changes in values
ticks = 0 #number of encoder value changes

while True: #spins motor and releases magnet
    motor1.throttle = -1 #spins motor at full speed
    if(button.value): #if kill switch is pressed
        motor1.throttle = 0 #turn off motor
    if (ch1.value == False and old1 == True): #if encoder values change False --> True
        ticks += 1
    old1 = ch1.value #save old encoder value
    rot = ticks/54 #ratio with gearbox and encoder ratio
    if (rot > 75 and math.fmod(ticks, 4) == 3): #if arm rotated correct number of times and arm is at correct position
        magnet.value = False #release payload
        motor1.throttle = 0 #turn off motor
        print("release")
        break #end code
    print("rots:")
    print(rot)
