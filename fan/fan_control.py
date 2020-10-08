#! /usr/bin/python3

from gpiozero import OutputDevice, CPUTemperature
import time
import lcddriver

cpu = CPUTemperature()

cpu_threshold_temp = 49
cpu_stable_temp = 45

fan = OutputDevice(17)

display = lcddriver.lcd()
display.lcd_clear()

while True:
    display.lcd_display_string("{} {}".format("CPU", cpu.temperature), 1)
    
    if cpu.temperature >= cpu_threshold_temp:
        fan.on()

    if cpu.temperature <= cpu_stable_temp:
        fan.off()

    time.sleep(1)
