#type: ignore
import board
import time
import digitalio
import pwmio

motor = pwmio.PWMOut(board.GP14, duty_cycle = 65535,frequency=5000)

release = digitalio.DigitalInOut(board.GP1)
release.direction = digitalio.Direction.OUTPUT
release.value = True

on = digitalio.DigitalInOut(board.GP0)
on.direction = digitalio.Direction.OUTPUT
on.value = True

speed = 0
encoder = 0
encoderMax = 50
rotation = 0
rotationMax = 15

while (speed < 65535):
    motor.duty_cycle = speed
    print(speed)
    speed += 5
    time.sleep(.001)
while speed > 0:
    print(encoder)
    print(rotation)
    if (encoder == encoderMax):
        rotation += 1
        encoder = 0
        if (rotation == rotationMax):
            release.value = False
            while (speed > 0):
                motor.duty_cycle = speed
                print(speed)
                speed -= 5
                time.sleep(.001)
