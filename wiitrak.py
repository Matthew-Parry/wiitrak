#!/usr/bin/python
#
# wiitrak.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
#
# Matthew Parry 2013
#
# Based on code by Matt Hawkins (raspberryspy)

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid		#module for connecting Wii remote
import bigtrak		#module for controlling bigtrak
import time
import os
import RPi.GPIO as GPIO


#Specify the direct to turn the motor
#Clockwise AIN1/BIN1 = HIGH and AIN2/BIN2 = LOW
#Counter-Clockwise: AIN1/BIN1 = LOW and AIN2/BIN2 = HIGH

button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
#    print 'Left pressed'
    bigtrak.setupPins()
    bigtrak.goleft(0.15)
    bigtrak.resetpins()
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
#    print 'Right pressed'
    bigtrak.setupPins()
    bigtrak.goright(0.15)
    bigtrak.resetpins()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
#    print 'Up pressed'    
    bigtrak.setupPins()
    bigtrak.goforwards(0.25)
    bigtrak.resetpins()    
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    #print 'Down pressed' 
    bigtrak.setupPins()
    bigtrak.gobackwards(0.25)
    bigtrak.resetpins()     
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    #print 'Button 1 pressed'
    os.system("mpg123 love.mp3")
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
   # print 'Button 2 pressed'
    os.system("mpg123 seven.mp3")
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
