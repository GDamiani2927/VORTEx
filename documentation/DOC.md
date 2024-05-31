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
Encoder values: ch1.value and ch2.value

#### Problems
Encoder values: The first issue was getting actual values from the encoders. We had never used the encoders on a REV motor with a Pico before so we experimented to find out how it would connect best. We found that Pico could read the Channel 1 and Channel 2 wires in the encoder cable by simply connecting them to a pin and declaring them as a digital input. They each would transmit True or False values depending on whether or not one of the magnets had spun by them, which we would use to find the number of rotations.

Rotations: The encoder's values could be used to indicate the number of revolutions by the axle but we had issues finding the correct ratio. Channel 1 and Channel 2 are the two signals the encoders send to the Pico, but Channel 2 is only necessary to find which direction the motor is spinning, which was not relevant to our project so we didn't use that wire. Channel 1 would send True or False values but we had to find how many times the wire read as True in one spin. The sources online all offered slightly different ratios but eventually using [this source] we found that there would be 4 channel raises in one rotation. After testing this by spinning the axle exactly once, we found that this produced the correct number of rotations based off the encoder values.

No signal from encoders: This was the most significant problem that we encountered and we still aren't 100% sure of the cause of this issue. The encoders just suddenly stopped sending signals to the Pico even though they had worked the day before. We checked all the wiring and code but couldn't find any problems that would make the encoder suddenly stop working. Even after connecting the motor to the REV Control Hub, there were no encoder signals. Then, we found [online] that some of the encoders on REV motor tended to move away from the magnets inside the motor so it wouldn't be able to detect any signals. To try to tix this, we took off the back cap of the motor and pushed the black encoder disk slightly toward the circuit board and the magnets, but without letting them touch and short out. Once we reconnected the encoder, it would show values on the REV Control Hub, but not on the Pico. We changed around the pins the encoder was connected to and then it would finally output signals to the Pico. This issue was most likely a combination of the encoder being slightly nudged away from the magnets inside the motor and the Pico not receiving the input on some of its pins.

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

### Code Test

![GIF](Conklin-Damiani-PITS/images/test1.gif)

#### Analysis
This test showed the first successful test of the entire code. As shown in the video, the launcher spins the arm 10 times and then releases the magnet when the encoders indicate that the arm is in the right spot, which would release the rocket in a real launch. Then, the arm stops and the code ends. This showed that we had solved several of our earlier problems. The Pico was able to track the number of revolutions the arm made, which was a problem early on because we couldn't find the exact ratio of encoder ticks to axle rotations. It also showed that the encoders were working again after the issue we had with the encoders not sening any signal to the pins. The code was also able to detect when the arm was at a specific position and released the magnet.

#### Launch Test

#### Analysis
