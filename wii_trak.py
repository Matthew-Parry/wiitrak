#!/usr/bin/python
#
# Matthew Parry April 2013
#
#
# based on wii_remote_1.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1101
# Author : Matt Hawkins
# Date   : 30/01/2013
# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time
import RPi.GPIO as GPIO

def goforwards(*ignore):
	#Declare the GPIO settings
	print "Set GPIO Board numbers"
	# to use Raspberry pi board pin numbers
	GPIO.setmode(GPIO.BOARD)

	# set up GPIO pins
	GPIO.setup(7, GPIO.OUT) #Connected to PWMA
	GPIO.setup(11, GPIO.OUT) #Connected to AIN2
	GPIO.setup(12, GPIO.OUT) #Connected to AIN1
	GPIO.setup(13, GPIO.OUT) #Connected to STBY
	GPIO.setup(15, GPIO.OUT) #Connected to BIN1
	GPIO.setup(16, GPIO.OUT) #Connected to BIN2
	GPIO.setup(18, GPIO.OUT) #Connected to PWMB
	#First we will drive everything clockwise
	#Set the direction of Motor A
	GPIO.output(12, GPIO.HIGH) #Set AIN1
	GPIO.output(11, GPIO.LOW) #Set AIN2
	#Set the Speed / PWM for A
	GPIO.output(7, GPIO.HIGH) #Set PWMA

	#Set the direction of Motor B
	GPIO.output(15, GPIO.HIGH) #Set BIN1
	GPIO.output(16, GPIO.LOW) #Set BIN2
	#Set the Speed / PWM for B
	GPIO.output(18, GPIO.HIGH) #Set PWMA

	#Make sure STBY is disabled - Set it to HIGH
	GPIO.output(13, GPIO.HIGH)
	
	time.sleep(2)
	
	#Now set everything to low (Switch everything Off)
	GPIO.output(12, GPIO.LOW) #Set AIN1
	GPIO.output(11, GPIO.LOW) #Set AIN2
	GPIO.output(7, GPIO.LOW) #Set PWMA
	GPIO.output(15, GPIO.LOW) #Set BIN1
	GPIO.output(16, GPIO.LOW) #Set BIN2
	GPIO.output(18, GPIO.LOW) #Set PWMA
	GPIO.output(13, GPIO.LOW) #Set STBY

	GPIO.cleanup()	#free all pins
	

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
    print 'Left pressed'
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'        
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'      
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    goforwards()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
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
