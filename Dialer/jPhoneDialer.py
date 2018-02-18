#/usr/bin/python

import serial # Library for serial port communications
import gi # Library for Python GObject introspection, the GTK Python bindings
gi.require_version('Gtk', '3.0') # Set the minimum compatible GTK+ version to 3.0, which is the testing environment
from gi.repository import Gtk # The GTK module

global DialerEntry # Declare the global variable that contains the telephone number input string
DialerEntry = "" # Initialize the telephone number string as empty

def AddNumber(number): # Local method to add a digit to the telephone number
	global DialerEntry # Declaration to use the global variable, not a new local one
	DialerEntry += number # Set the string to itself with the additional number concatenated to the end of it
	entrybox.set_text(DialerEntry) # Set the telephone number entry box widget to the modified string

class Handler:
	def WindowDestroyed(self, *args):
		Gtk.main_quit(*args)

	def ClickedDelete(self, *args):
		global DialerEntry # Use global variable in this function, not local which is the default
		DialerEntry = DialerEntry[:-1] # Remove the last character from the character array
		entrybox.set_text(DialerEntry) # Set the DialerEntry text to the resulting string 

	def ClickedOne(self, *args):
		AddNumber("1")

	def ClickedTwo(self, *args):
		AddNumber("2")

	def ClickedThree(self, *args):
		AddNumber("3")

	def ClickedFour(self, *args):
		AddNumber("4")

	def ClickedFive(self, *args):
		AddNumber("5")

	def ClickedSix(self, *args):
		AddNumber("6")

	def ClickedSeven(self, *args):
		AddNumber("7")

	def ClickedEight(self, *args):
		AddNumber("8")

	def ClickedNine(self, *args):
		AddNumber("9")

	def ClickedZero(self, *args):
		AddNumber("0")

	def ClickedStar(self, *args):
		AddNumber("*")

	def ClickedPound(self, *args):
		AddNumber("#")

	def ClickedCall(self, *args):
# Open communication with serial port
		ser = serial.Serial(port='/dev/serial0', baudrate=115200, timeout=1)
# Dial number entered
		cmd="ATD"+DialerEntry+";\r"
		ser.write(cmd.encode())
		msg=ser.read(64)
		print(msg)
		if msg == "NO CARRIER":
			# Modal dialog box to notify user the call failed
			dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Call Failed")
			dialog.format_secondary_text("Click OK to acknowledge.")
			dialog.run()
			dialog.destroy()
			ser.close() # Close the serial connection, to free it up for later
		else:
# Show status dialog
			dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Attempting to dial "+DialerEntry+"...")
			dialog.format_secondary_text("Click OK to hang up.")
			dialog.run()
			print("INFO dialog closed")
			dialog.destroy()
# Prepare to hang up
			cmd="AT+CVHU=0\r"
			ser.write(cmd.encode())
			msg=ser.read(64)
			print(msg)
# Hang up
			cmd="ATH\r"
			ser.write(cmd.encode())
			msg=ser.read(64)
			print(msg)
			ser.close() # Close the serial port
# End Handler class
		
# Create window from XML template, connect signals to handler class and methods
builder = Gtk.Builder()
builder.add_from_file("/home/pi/Documents/jPhone/Dialer/jPhoneDialer.glade")
builder.connect_signals(Handler())

# Associate widgets with variables, and make window visible
entrybox = builder.get_object("EntryDial")
window = builder.get_object("MainWindow")
window.show_all()

# Call GTK+ library initialization
Gtk.main()

# Transition to in-call interface application once call is placed
