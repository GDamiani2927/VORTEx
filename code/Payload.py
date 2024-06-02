#type: ignore
import time
import board
import adafruit_mpu6050 #accelerometer library
import busio #I2c library

i2c = busio.I2C(board.GP5, board.GP4) #I2c declaration
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #accelerometer declaration

with open("/data.csv", "a") as datalog: #connects datalog to data.csv file
    while True: #gathers acceleration data
        runtime = time.monotonic() #total runtime
        xacc = mpu.acceleration[0] #x acceleration
        yacc = mpu.acceleration[1] #y acceleration
        zacc = mpu.acceleration[2] #z acceleration
        datalog.write(f"{runtime},{xacc},{yacc},{zacc}\n") 
        datalog.flush() #pushes acceleration data to data.csv
        time.sleep(.25)
