# Add your Python code here. E.g.
from microbit import *
#imports the microbit radio library
import radio

radio.on()
#configures the channel on which channel to transmit information
radio.config(channel=10)


while True:
    #get´s x and y values from the micobit
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    #if the y or x value are larger or smaller than 180, send message
    if y>180
        radio.send("down")
       
    elif y<-180
        radio.send("up")
        
    elif x>180
        radio.send("left")
       
    elif x<-180
        radio.send("right")
    #if both values correspond, send messsage
    if x>180 and y>180
        radio.send("br")
    
    if x<-180 and y<-180
        radio.send("tl")
    
    if x<-180 and y>180
        radio.send("bl")
    
    if x>180 and y<-180
        radio.send("tr")    
      #if a button is pressed send message and delay  
    if button_a.is_pressed():
        radio.send("plus")
        sleep(50)
        
    if button_b.is_pressed():
        radio.send("minus")
        sleep(50)
