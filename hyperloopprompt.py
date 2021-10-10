'''
The CPP Hyperloop Pod is accelerating to a speed of 200 mph from an initial velocity of 0 mph, 
which takes about 7200 milliseconds of time. If the time is at a multiple of 100 ms, we will retrieve 
a data point from the IMU. If the time is at a multiple of 750 ms, we will retrieve a data point from 
the DS18B20 Temperature Sensor. If the time is exactly at 5000ms, the pod will autonomously retract 
its brakes and prepare for travel at full speed. When the pod reaches maximum speed, it will print 
out the number of data points from the IMU and the number of data points from the temp sensor that 
that pod system took over the course of its startup sequence.
'''

import time

for x in range(0,7200):
    if x % 100 == 0:
        print(f"IMU Data Retrieved at {x}")
    
    if x % 750 == 0:
        print(f"Temp Data Retrieved at {x}")

    if x == 5000:
        print(f"Brakes Retracted! at {x}")
