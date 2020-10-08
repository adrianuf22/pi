#! /usr/bin/python3

from . import lcddriver

display = lcddriver.lcd()
display.lcd_clear()

def print_msg(msg):
    display.lcd_display_string(msg, 1)