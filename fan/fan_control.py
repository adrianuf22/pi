#! /usr/bin/python3

import time
from gpiozero import OutputDevice, CPUTemperature

from i2c.print_msg import print_msg

cpu = CPUTemperature()

cpu_threshold_temp = 49
cpu_stable_temp = 45

fan = OutputDevice(17)

while True:
    print_msg("{} {}".format("CPU", cpu.temperature))
    
    if cpu.temperature >= cpu_threshold_temp:
        fan.on()

    if cpu.temperature <= cpu_stable_temp:
        fan.off()

    time.sleep(1)
