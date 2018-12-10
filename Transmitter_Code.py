# Add your Python code here. E.g.
from microbit import *
#imports the microbit radio library
import radio

#turns the microbit radio on
radio.on()
#sets the channel the radio will transmit at
radio.config(channel=10)


while True:
    #creates a variable so i dont have to write som much
    gesture = accelerometer.current_gesture()
    #if the microbit is tilting upwards, send "down"
    if gesture == "face up":
        radio.send("down")
        
    #if the microbit is tilting downwards, send "up"
    elif gesture == "face down":
        radio.send("up")
        
    #if the microbit is tilting left, send "left"    
    elif gesture == "left":
        radio.send("left")
        
    #if the microbit is tilting right, send "right"    
    elif gesture == "right":
        radio.send("right")
        
    #if button a is pressed send "plus"  
    if button_a.is_pressed():
        radio.send("plus")
        #makes the microbit stop for 0.5 seconds
        sleep(50)
        
    #if button b is pressed send "minus"
    if button_b.is_pressed():
        radio.send("minus")
        #makes the microbit stop for 0.5 seconds
        sleep(50)
