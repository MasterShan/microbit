# Add your Python code here. E.g.
from microbit import *
#imports the microbit radio library
import radio

radio.on()
radio.config(channel=10)


while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    
    if y>180
        radio.send("down")
       
    elif y<-180
        radio.send("up")
        
    elif x>180
        radio.send("left")
       
    elif x<-180
        radio.send("right")
    
    if x>180 and y>180
        radio.send("br")
    
    if x<-180 and y<-180
        radio.send("tl")
    
    if x<-180 and y>180
        radio.send("bl")
    
    if x>180 and y<-180
        radio.send("tr")    
        
    if button_a.is_pressed():
        radio.send("plus")
        sleep(50)
        
    if button_b.is_pressed():
        radio.send("minus")
        sleep(50)
