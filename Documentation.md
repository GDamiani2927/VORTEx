# Documentation

## Table of Contents
* [CAD](#cad)
* [Code](#code)
* [Wiring](#wiring)
* [Data](#data)
* [Tests](#tests)

## CAD

### Renderings

### Analysis

## Code

### Launcher 

[Launcher Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/SpinLaunch.py)

### Rocket

[Rocket Code](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/Rocket.py)

The rocket code was very straightforward and was one of the simplest parts of this project because the code was identical to the Data Storage assignment we completed earlier in the year. The code's only job is to track the acceleration of the rocket so we were able to completely reuse the code from the Data Storage assignment.

Data:

Accelerometer:



## Wiring

## Tests

### Test 1

![GIF](images/test1.gif)

This test showed the first successful test of the entire code. As shown in the video, the launcher spins the arm 10 times and then releases the magnet when the encoders indicate that the arm is in the right spot, which would release the rocket in a real launch. Then, the arm stops and the code ends. This showed that we had solved several of our earlier problems. The Pico was able to track the number of revolutions the arm made, which was a problem early on because we couldn't find the exact ratio of encoder ticks to axle rotations. It also showed that the encoders were working again after the issue we had with the encoders not sening any signal to the pins. The code was also able to detect when the arm was at a specific position and released the magnet.

## Data

### Analysis

