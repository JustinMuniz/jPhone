#/usr/bin/python

import serial
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

global DialerEntry
DialerEntry = ""

def AddNumber(number):
	global DialerEntry
	DialerEntry += number
	entrybox.set_text(DialerEntry)

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
