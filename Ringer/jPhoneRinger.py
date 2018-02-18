#/usr/bin/python

# Load and configure GTK+ 3 support
import gi # Library for Python GObject introspection, the GTK Python bindings
gi.require_version('Gtk', '3.0') # Set the minimum compatible GTK+ version to 3.0, which is the testing environment
from gi.repository import Gtk # The GTK module

# Load and configure GPIO support
import RPi.GPIO as GPIO  # GPIO library to read / set GPIO pin in / out
GPIO.setmode(GPIO.BCM)   # Set GPIO pin numbering mode
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO 4 set up as input. It is pulled up to match the FONA RI default status  

import serial # Library for serial port communications
import sys # Library for exiting python
from time import sleep # Library for passing a specific number of time before continuing the script

class Handler: # Class with methods connected to the GTK widget signals
	def ClickedAnswer(self, *args): # Method called when Answer button is clicked
		# Replace with in-call interface
		# Tell modem to answer the call
		cmd="ATA"
		ser.write(cmd.encode())
		msg=ser.read(64)
		if msg == "NO CARRIER":
			# Modal dialog box to notify user the call failed
			dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Call Failed")
			dialog.format_secondary_text("Click OK to acknowledge.")
			dialog.run()
			dialog.destroy()
			ser.close() # Close the serial connection, to free it up for later
			window.destroy() # Close the window
		else:
			# Modal dialog box to hang up
			dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Call Answered")
			dialog.format_secondary_text("Click OK to hang up.")
			dialog.run()
			dialog.destroy()
			ser.close() # Close the serial connection, to free it up for the HangUp method
			HangUp() # Hang up voice call
	def ClickedDecline(self, *args): # Method called when Decline button is clicked
		HangUp() # Hang up voice call
# End Handler class

Gtk.main() # Call GTK+ library initialization

def CleanUp(ExitStatus): # Local method to free up resources and exit Python
	GPIO.cleanup() # clean up GPIO on CTRL+C exit
	Gtk.main_quit(*args) # Clean up GTK
	sys.exit(ExitStatus) # Provide the exit status to Python and exit Python

def HangUp(): # Local Method to instruct modem to hang up a voice call
	ser = serial.Serial(port='/dev/serial0', baudrate=115200, timeout=1) # Open communication with serial port
	# Prepare to hang up
	cmd="AT+CVHU=0\r"
	ser.write(cmd.encode())
	msg=ser.read(64)
	# Hang up
	cmd="ATH\r"
	ser.write(cmd.encode())
	msg=ser.read(64)
	ser.close() # Close the serial connection, to free it up for later
	window.destroy() # Close the window

while (true): # Program should only be closed by a system exit or on error, so it will loop indefinitely
	try: # Ensure a way to catch exceptions
		GPIO.wait_for_edge(4, GPIO.FALLING) # Wait until BCM pin 4 starts trending towards low
		sleep(0.12) # Wait 120ms
		if GPIO.input(4) == GPIO.HIGH:# Probe BCM pin 4 to check if it returned to high
#			 # Run script to notify of incoming text message
		else: # If BCM pin 4 is still falling or low after 120ms it is a phone call
			# Create window from XML template, connect signals to handler class and methods
			builder = Gtk.Builder()
			builder.add_from_file("/home/pi/Documents/jPhone/Ringer/jPhoneRinger.glade")
			builder.connect_signals(Handler())
			# Associate widgets with variables, and make window visible
			LabelCaller = builder.get_object("GtkLabelCaller") # Create a reference to the Caller ID label, to set its text contents
#			 # Determine the phone number of the caller
#			 # Compare the phone number of the caller to those in the contacts list
#			 # Set the Caller ID label to the caller name or phone number
			window = builder.get_object("MainWindow") # Create a reference to the Window, to make it visible
			window.show_all() # Make the incoming call interface visible
			# Sound ringer
			# Flash LED
			# Turn on Display?
			# Wait for pin 4 to go gigh
			# Close window when call is answered or hung up
	except SystemExit: # Give up on waiting if Python receives instructions to terminate from the operating system
		CleanUp() # Run the clean up function to free resources

# Write scripts to add and remove ringer from system's boot process
