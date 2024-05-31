#type: ignore
import time
import board
import adafruit_mpu6050 
import busio

i2c = busio.I2C(board.GP5, board.GP4)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

with open("/data.csv", "a") as datalog: 
    while True:
        runtime = time.monotonic()
        xacc = mpu.acceleration[0] 
        yacc = mpu.acceleration[1] 
        zacc = mpu.acceleration[2] 
        datalog.write(f"{runtime},{xacc},{yacc},{zacc}\n") 
        datalog.flush()
        time.sleep(.25)
