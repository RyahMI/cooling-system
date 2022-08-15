from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
sleep(1000)

while True:
    add_text(0, 0, "Temp:")
    add_text(0, 1, str(temperature()))


    if button_a.was_pressed():
        display.scroll(temperature())
    
    if temperature() > 25:
        pin0.write_digital(1)
        add_text(0, 2, "Fan: On")
    else:
        pin0.write_digital(0)
        add_text(0, 2, "Fan: Off")

        
    