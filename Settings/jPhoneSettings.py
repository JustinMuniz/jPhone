#/usr/bin/python

import serial # Library for serial port communications
import gi # Library for Python GObject introspection, the GTK Python bindings
gi.require_version('Gtk', '3.0') # Set the minimum compatible GTK+ version to 3.0, which is the testing environment
from gi.repository import Gtk # The GTK module

class Handler:
	def WindowDestroyed(self, *args):
		Gtk.main_quit(*args)
	def ClickedUpdateOS(self, *args):
		placeholder = 1
	def ClickedUpdatejPhone(self, *args):
		placeholder = 1
	def ClickedUpdateSoftware(self, *args):
		placeholder = 1
	def ClickedRepairjPhone(self, *args):
		placeholder = 1
	def ClickedRepairFS(self, *args):
		placeholder = 1
	def ClickedInstallDT(self, *args):
		placeholder = 1
	def ClickedRemoveDT(self, *args):
		placeholder = 1
	def ClickedResetModem(self, *args):
		placeholder = 1
	def StateSetAirplaneMode(self, *args):
		placeholder = 1
	def StateSetWiFi(self, *args):
		placeholder = 1
	def StateSetBluetooth(self, *args):
		placeholder = 1
	def StateSetCellularData(self, *args):
		placeholder = 1
	def ChangedScreenTimeout(self, *args):
		placeholder = 1
# End Handler class

# Create window from XML template
Builder = Gtk.Builder()
Builder.add_from_file("/home/pi/Documents/jPhone/Settings/jPhoneSettings.glade")
Builder.connect_signals(Handler()) # Connect signals to handler class and methods

# Associate widgets with variables
Window = Builder.get_object("GtkWindowMain")
HostnameValue = Builder.get_object("GtkLabelHostnameValue")
PhoneDeveloperValue = Builder.get_object("GtkLabelPhoneDeveloperValue")
PhoneModelValue = Builder.get_object("GtkLabelPhoneModelValue")
ModemManufacturerValue = Builder.get_object("GtkLabelModemManufacturerValue")
ModemModelValue = Builder.get_object("GtkLabelModemModelValue")
IMEIValue = Builder.get_object("GtkLabelIMEIValue")
LabelICCIDValue = Builder.get_object("GtkLabelICCIDValue")
PhoneNumberValue = Builder.get_object("GtkLabelPhoneNumberValue")
CellularNetworkValue = Builder.get_object("GtkLabelCellularNetworkValue")
SignalStrengthValue = Builder.get_object("GtkLabelSignalStrengthValue")
TotalInternalStorageValue = Builder.get_object("GtkLabelTotalInternalStorageValue")
AvailableInternalStorageValue = Builder.get_object("GtkLabelAvailableInternalStorageValue")
BatteryLevelValue = Builder.get_object("GtkLabelBatteryLevelValue")
SystemUptimeValue = Builder.get_object("GtkLabelSystemUptimeValue")
TimeSinceFullChargeValue = Builder.get_object("GtkLabelTimeSinceFullChargeValue")
ProcessorValue = Builder.get_object("GtkLabelProcessorValue")
MemoryValue = Builder.get_object("GtkLabelMemoryValue")
GraphicsValue = Builder.get_object("GtkLabelGraphicsValue")
jPhoneVersionValue = Builder.get_object("GtkLabeljPhoneVersionValue")
LinuxVersionValue = Builder.get_object("GtkLabelLinuxVersionValue")
PythonVersionValue = Builder.get_object("GtkLabelPythonVersionValue")
GTKVersionValue = Builder.get_object("GtkLabelGTKVersionValue")
SwitchAirplaneMode = Builder.get_object("GtkSwitchAirplaneMode")
SwitchWiFi = Builder.get_object("GtkSwitchWiFi")
SwitchBluetooth = Builder.get_object("GtkSwitchBluetooth")
SwitchCellularData = Builder.get_object("GtkSwitchCellularData")
ComboBoxScreenTimeout = Builder.get_object("GtkComboBoxScreenTimeout")

# Determine information and toggle values, and set them
placeholder=1

Window.show_all() # Make window visible

# Call GTK+ library initialization
Gtk.main()
