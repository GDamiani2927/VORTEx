## DISCLAIMER: This is not real data.
And we are not trying to pass it off as such. This is a simulation of what our data would likely look like (and an analysis of said simulation) had we been able to record it. The data that we recorded for our data collecting launch on 5/31 was lost along with the rest of the files on the board. The reason for this data loss is still uncclear, as the videos do not show a particularly hard landing for the last launch. That said, fuether troubleshooting to determine the root cause of this issue will be performed, and a new issue will be created.
## Data
The simulated data simulates a behavior similar to that of the actual launches in the format of the data that was supposed to be recorded. As demonstrated in Payload.py, the data is recorded to a CSV entitled "data" by the MPU 6050 accelerometer in the format of t (time in seconds),x (acceleration in meters/sec^2),y (acceleration in meters/sec^2),z (acceleration in meters/sec^2).

The orientation of the gyroscope is planar with the Pico, and the x y and z acceleration values are local to this orientation. See the image for a depiction of the directions.

![Axes](https://github.com/GDamiani2927/Conklin-Damiani-PITS/blob/main/images/Axes.png)
