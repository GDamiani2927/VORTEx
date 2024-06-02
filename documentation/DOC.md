# Documentation

## Table of Contents
* [CAD](#cad)
* [Code](#code)
* [Wiring](#wiring)
* [Data](#data)
* [Tests](#tests)

## CAD
### Launcher

[Launcher CAD](https://cvilleschools.onshape.com/documents/1d00744b82773202e76274bb/w/be73ad2991f912dc77e25081/e/d71a1bd423725bcd32285f1e)

#### Overview
The launcher is our name for the bulk of the project, the mechanism to launch the payload. The launcher harnesses the power of angular velocity by spinning up a beam at a high rate and then detaching the payload at a specified time. This method of launching allows us to consistently launch the payload without having to power the payload itself. Without having to use onboard thrust, we can greatly simplify the launching process.
#### Components
Motor Casing: The base of the launcher that holds the motor and attaces to the central axle. Contains a 90 Degree gearbox to transfer power from the vertical to horizontal plane. Furthermore, the motor casing has mounting holes for easy attachment to whatever base best suits the launcher.

Beam: The beam of the launcher is the wing shaped structure that rotates around the center of rotation. One end of the beam contains the electromagnet to attach to the rocket, whereas the other end contains a large counterweight to counterract the stress of the electromagnet and payload.
#### Challenges
Counterweighting Beam: On one end of the beam, the rocket and electromagnet add considerable weight imbalance. Furthermore, the opposite side of the beam cannot be very long, as the print bed of our 3d printers could not facilitate anything nearly as long as the payload end. The solution we landed on was creating a counterweight holder on the other end where we could add various different weights at different distances from the center to perfect our balance of the beam.

Reinforcing Base: When the beam spins at high RPMs, the torque bucks the entire launcher back and forth. To reinforce the base, we attached the motor casing to a wide piece of wood, weighed down by two large masses. This allows us to easily set up and dismantle the launcher on nearly any surface and still get somewhat consistent launch conditions.
#### Analysis
Overall, the design of the launcher is pretty good. It has all the basics required for a semi-consistent launch and has had pretty good performance. That said, there are many aspects that could be improved. Firstly, the high center of gravity of the motor casing results in instability. In the long run this could be remedied by changing the motor to lying flat near the base of the launcher. Secondly, the design is not particularly flexible. It wasn't designed with assembly and disassembly in mind, and as a result it creates a large undertaking any time modifications are in order. Just as an examble of this, it took two entire days to assemble and dissassemble the entire thing to swap out the old slip ring for the new one. In the future, when the launcher is not in constant testing, the design should be improved to allow for ease of both operation and maintenance.
### Payload
#### Components
#### Analysis
## Code

### Launcher 

[Launcher Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/SpinLaunch.py)

#### Overview
The code for the launcher allows the arm to spin and detach the payload so that it is launched and can gather data. It starts by turning on the electromagnet, which holds the payload connected to the arm, and then spinning the motor up to max speed. The code counts the number of rotations by using the encoders built into the motor and once the arm has rotated the set amount, the magnet is turned off, which detached the payload and launches it. The code is relatively straightforward but we ran into several issues with the encoders. 

#### Components
Motor: declared in pwmio library and controlled with motor1.throttle = 1 or motor1.throttle = 0                                              
Encoder values: received and read with ch1.value and ch2.value                                                                               
Magnet: controlled with digital output magnet.value = True or magnet.value = False
Kill switch: turns off motor if button.value reads as True

#### Challenges
Encoder values: The first issue was getting actual values from the encoders. We had never used the encoders on a REV motor with a Pico before so we experimented to find out how it would connect best. We found that Pico could read the Channel 1 and Channel 2 wires in the encoder cable by simply connecting them to a pin and declaring them as a digital input. They each would transmit True or False values depending on whether or not one of the magnets had spun by them, which we would use to find the number of rotations.

Rotations: The encoder's values could be used to indicate the number of revolutions by the axle but we had issues finding the correct ratio. Channel 1 and Channel 2 are the two signals the encoders send to the Pico, but Channel 2 is only necessary to find which direction the motor is spinning, which was not relevant to our project so we didn't use that wire. Channel 1 would send True or False values but we had to find how many times the wire read as True in one spin. The sources online all offered slightly different ratios but eventually using [this source](https://docs.revrobotics.com/duo-control/sensors/encoders/motor-based-encoders) we found that there would be 4 channel raises in one rotation. The encoder would switch from False to True when the magnet passes by the encoder so by counting how many times the values changed, we could find the number of rotations. After testing this by spinning the axle exactly once, we found that this produced the correct number of rotations based off the encoder values.

No signal from encoders: This was the most significant problem that we encountered and we still aren't 100% sure of the cause of this issue. The encoders just suddenly stopped sending signals to the Pico even though they had worked the day before. We checked all the wiring and code but couldn't find any problems that would make the encoder suddenly stop working. Even after connecting the motor to the REV Control Hub, there were no encoder signals. Then, we found [online](https://www.reddit.com/r/FTC/comments/s3wexw/motors_not_running_after_trying_to_use_encoders/) that some of the encoders on REV motor tended to move away from the magnets inside the motor so it wouldn't be able to detect any signals. To try to tix this, we took off the back cap of the motor and pushed the black encoder disk slightly toward the circuit board and the magnets, but without letting them touch and short out. Once we reconnected the encoder, it would show values on the REV Control Hub, but not on the Pico. We changed around the pins the encoder was connected to and then it would finally output signals to the Pico. This issue was most likely a combination of the encoder being slightly nudged away from the magnets inside the motor and the Pico not receiving the input on some of its pins.

#### Analysis
Overall, the code worked successfully when put together with the launcher and rocket. The encoders were by far the most difficult part but once those issues were solved, the rest of the code was relatively straightforward. We had only used the built-in encoders in the REV motors with the REV Control Hub, so it took a while to figure out how to wire and receive data from the encoders. We also learned that by using a transistor and an external power supply to control the voltage, we can control the magnet by sending it True/False signals like any other digital output that would turn it on and off. The launcher releases the payload when the encoders show that the arm has rotated enough times but also when the arm is in the correct position, however we suspect that there is a small degree of inaccuracy because the change in encoder values is occasionally not detected. This would make the arm over-rotate a bit and this is hard to fix because it is not a reliable bug and is hard to detect because it does not have a great impact on the release time. Also, the code starts measuring arm positioning from whatever position the motor begins in, so if the arm does not begin in the same spot every time, the launcher will release the rocket differently with each launch. However, this does not have a huge effect on the launch because the counterweight on the arm is heavy enough to ensure that the motor starts in the same position. The code for the launcher had several problems and bugs that we were almost entirely able to fix so that the arm would launch the payload at the correct time and position.

### Payload

[Payload Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/Payload.py)

#### Overview
The payload is attached to the end of the launcher arm and is what we use to gather data. It is launched into the air and an accelerometer will gather acceleration in the z, y, and z directions while it is in data mode. Then, we use the data.csv file on the Pico to graph the acceleration.

#### Components
Accelerometer: uses adafruit_mpu6050 library with mpu.acceleration[x] to find acceleration for x, y, and z                                   
Data Storage: pushes accelerometer data to data.csv with datalog.flush()

#### Analysis
The payload code was very straightforward and was one of the simplest parts of this project because the task was similar to the Data Storage assignment we completed earlier in the year. The code needed to track and store the acceleration of the payload so we were able to completely reuse the code from the Data Storage assignment. The payload uses an accelerometer to find the acceleration of the Pico in the x, y, and z directions when it is placed in data mode. Then, when it is put back into code mode, the acclerometer data is saved onto the Pico's data.csv file. From there, the data from the accelerometer is graphed so that we can access and interpret it.

## Wiring

### Launcher
![Image](/images/launcher_wiring.jpeg)

#### Components
Power supply                                                                                                                                
2 9V battery packs                                                                                                                          
REV HD Hex Motor                                                                                                                            
H-Bridge                                                                                                                                    
Electromagnet                                                                                                                               
Kill switch                                                                                                                                 
Pico battery

#### Analysis

### Payload
![Image](/images/payload_wiring.jpeg)

#### Components
Accelerometer                                                                                                                               
Pico battery

#### Analysis
The wiring for the payload was quite simple because it only contained an accelerometer and a Pico battery. It was also identical to the wiring for the Data Storage assignment, so we did not have many issues with it. We wired the accelerometer and battery so that they would fit inside the payload during launches. The Pico rails were accessible through 2 slits in the body of the payload so that we could use a switch to change the Pico between data mode and code mode. The wiring had to be very compact and secure so that it would fit in the payload without disconnecting.

## Tests

### Code Test

![GIF](/images/test1.gif)

#### Analysis
This test showed the first successful test of the entire code. As shown in the video, the launcher spins the arm 10 times and then releases the magnet when the encoders indicate that the arm is in the right spot, which would release the rocket in a real launch. Then, the arm stops and the code ends. This showed that we had solved several of our earlier problems. The Pico was able to track the number of revolutions the arm made, which was a problem early on because we couldn't find the exact ratio of encoder ticks to axle rotations. It also showed that the encoders were working again after the issue we had with the encoders not sening any signal to the pins. The code was also able to detect when the arm was at a specific position and released the magnet.

### Launch Test

![GIF](/images/test2.gif)

#### Analysis
This test showed our first official launch with the finished code and CAD designs. We had already determined that the arm would spin but we hadn't tested releasing the rocket while spinning yet. We had issues with the transister so Gabe had to release the electromagnet manually by estimating when the arm was on an upward arc and turning off the power supply to the electromagnet, which would release the rocket. The test was successful because it showed that the electromagnet would release the rocket very quickly and the rocket flew off the launcher. This test showed that all the different parts of the project that we had been working on separately were able to work together and didn't cause any issues. We didn't gather data from the rocket for this test because we were just testing the launcher.
