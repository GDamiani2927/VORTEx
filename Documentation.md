# Documentation

## Table of Contents
* [CAD](#cad)
* [Code](#code)
* [Wiring](#wiring)
* [Data](#data)
* [Tests](#tests)

## CAD

## Code

### Launcher 

[Launcher Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/SpinLaunch.py)

#### Components

#### Problems

#### Analysis


### Rocket

[Rocket Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/Rocket.py)

#### Components
Accelerometer: uses adafruit_mpu6050 library with mpu.acceleration[x] to find acceleration for x, y, and z                                   
Data Storage: pushes accelerometer data to data.csv with datalog.flush()

#### Analysis
The rocket code was very straightforward and was one of the simplest parts of this project because the task was similar to the Data Storage assignment we completed earlier in the year. The code needed to track and store the acceleration of the rocket so we were able to completely reuse the code from the Data Storage assignment. The rocket uses an accelerometer to find the acceleration of the Pico in the x, y, and z directions when it is placed in data mode. Then, when it is put back into code mode, the acclerometer data is saved onto the Pico's data.csv file. From there, the data from the accelerometer is graphed so that we can access and interpret it.

## Wiring

## Data

### Analysis

## Tests

### Test 1

![GIF](images/test1.gif)

#### Analysis
This test showed the first successful test of the entire code. As shown in the video, the launcher spins the arm 10 times and then releases the magnet when the encoders indicate that the arm is in the right spot, which would release the rocket in a real launch. Then, the arm stops and the code ends. This showed that we had solved several of our earlier problems. The Pico was able to track the number of revolutions the arm made, which was a problem early on because we couldn't find the exact ratio of encoder ticks to axle rotations. It also showed that the encoders were working again after the issue we had with the encoders not sening any signal to the pins. The code was also able to detect when the arm was at a specific position and released the magnet.
