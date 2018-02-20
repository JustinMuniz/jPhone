#/usr/bin/python

# Load and configure GPIO support
try:
    import RPi.GPIO as GPIO # GPIO library to read / set GPIO pin in / out
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)   # Set GPIO pin numbering mode
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO 23 set up as input. It is pulled up to match the FONA RI default status  

import serial # Library for serial port communications
import sys # Library for exiting python
from time import sleep # Library for passing a specific number of time before continuing the script
from subprocess import call# Library for executing external processes and monitoring them

def CleanUp(ExitStatus): # Local method to free up resources and exit Python
	GPIO.cleanup() # clean up GPIO on CTRL+C exit
	sys.exit(ExitStatus) # Provide the exit status to Python and exit Python

ser = serial.Serial(port='/dev/serial0', baudrate=115200, timeout=1) # Open communication with serial port

# Tell modem to set RI pin low for 100-120ms on SMS receipt
cmd="AT+CFGRI=1\r" # Prepare instruction string to be sent to modem via the serial port
ser.write(cmd.encode()) # Send an encoded string to the modem
msg=ser.read(64) # read back the response from the modem

# Reset RI pin of serial port
cmd="AT+CRIRS\r" # Prepare instruction string to be sent to modem via the serial port
ser.write(cmd.encode()) # Send an encoded string to the modem
msg=ser.read(64) # read back the response from the modem

ser.close() # Close the serial connection, to free it up for later

try: # Ensure a way to catch exceptions
	while True: # Program should only be closed by a system exit or on error, so it will loop indefinitely
		GPIO.wait_for_edge(23, GPIO.FALLING) # Wait until BCM pin 23 starts trending towards low
		sleep(0.12) # Wait 120ms
		if GPIO.input(23) == GPIO.HIGH:# Probe BCM pin 23 to check if it returned to high
#			 # Run script to notify of incoming text message
			placeholder = 1
		else: # If BCM pin 23 is still falling or low after 120ms it is a phone call
			# Figure out how to do this without waiting for execution of child to finish
			call(["python", "/home/pi/Documents/jPhone/Ringer/jPhoneRinger.py"]) # Run script to display incoming call interface
except SystemExit: # Give up on waiting if Python receives instructions to terminate from the operating system
	CleanUp() # Run the clean up function to free resources
#print("Something is wrong") # Debug status

# Write scripts to add and remove ringer from system's boot process
