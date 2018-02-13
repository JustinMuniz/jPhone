// Dependencies
#include <gtk/gtk.h>
//#include <stdio.h>
//#include <string.h>
#include <unistd.h>			//Used for UART
#include <fcntl.h>			//Used for UART
#include <termios.h>		//Used for UART

// Global Variables
gchar DialerEntry[100] = "";
int DialerIndex = 0;
GtkWidget *GtkWidgetEntry;
GtkWidget *GtkWidgetWindow;

// Build the window
int main(int argc, char *argv[]) {
	// Declare variables
	GtkBuilder *GtkBuilderInstance; 

 
	// Initialize GTK and pass arguements
	gtk_init(&argc, &argv);
 
	// Create a Gtk Builder and populate it with the glade file
	GtkBuilderInstance = gtk_builder_new();
	gtk_builder_add_from_file (GtkBuilderInstance, "jPhoneDialer.glade", NULL);
 
	// Instanciate the window, and connect the signals for the widgets
	GtkWidgetWindow = GTK_WIDGET(gtk_builder_get_object(GtkBuilderInstance, "MainWindow"));
	GtkWidgetEntry = GTK_WIDGET(gtk_builder_get_object(GtkBuilderInstance, "EntryDial"));
	gtk_builder_connect_signals(GtkBuilderInstance, NULL);
 
    g_object_unref(GtkBuilderInstance);
 
    gtk_widget_show(GtkWidgetWindow);                
    gtk_main();
  
    return 0;
} // End main
 
// Called when window is closed
void WindowDestroyed() {
	// Terminate application
	gtk_main_quit();
} // End WindowDestroyed

// Called when ButtonOne is clicked
void ClickedOne() {
	DialerEntry[DialerIndex] = '1';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedOne 

// Called when ButtonTwo is clicked
void ClickedTwo() {
	DialerEntry[DialerIndex] = '2';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedTwo 

// Called when ButtonThree is clicked
void ClickedThree() {
	DialerEntry[DialerIndex] = '3';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedThree

// Called when ButtonFour is clicked
void ClickedFour() {
	DialerEntry[DialerIndex] = '4';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedFour

// Called when ButtonFive is clicked
void ClickedFive() {
	DialerEntry[DialerIndex] = '5';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedFive

// Called when ButtonSix is clicked
void ClickedSix() {
	DialerEntry[DialerIndex] = '6';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedSix

// Called when ButtonSeven is clicked
void ClickedSeven() {
	DialerEntry[DialerIndex] = '7';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedSeven

// Called when ButtonEight is clicked
void ClickedEight() {
	DialerEntry[DialerIndex] = '8';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedEight

// Called when ButtonNine is clicked
void ClickedNine() {
	DialerEntry[DialerIndex] = '9';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedNine

// Called when ButtonZero is clicked
void ClickedZero() {
	DialerEntry[DialerIndex] = '0';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedZero

// Called when ButtonStar is clicked
void ClickedStar() {
	DialerEntry[DialerIndex] = '*';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedStar

// Called when ButtonPound is clicked
void ClickedPound() {
	DialerEntry[DialerIndex] = '#';
	if (DialerIndex < 99)
		DialerIndex++;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedPound

// Called when ButtonDelete is clicked
void ClickedDelete() {
	if (DialerIndex > 0) {
		DialerIndex--;
	}
	DialerEntry[DialerIndex] = 0;
	gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
} // End ClickedDelete

// Called when ButtonCall is clicked
void ClickedCall() {

	// Check to see if there is a null phone number
	// Verify phone number is numeric
	// Verify that phone number is dialable

	//char * paramsList[] = {"/bin/bash", "-c", "printf \"ATD%s;\r\n\" \"$number\" > /dev/serial0",NULL};
	//execv ("/bin/bash", paramsList);


	//-------------------------
	//----- SETUP USART 0 -----
	//-------------------------
	//At bootup, pins 8 and 10 are already set to UART0_TXD, UART0_RXD (ie the alt0 function) respectively
	int uart0_filestream = -1;
	
	//OPEN THE UART
	//The flags (defined in fcntl.h):
	//	Access modes (use 1 of these):
	//		O_RDONLY - Open for reading only.
	//		O_RDWR - Open for reading and writing.
	//		O_WRONLY - Open for writing only.
	//
	//	O_NDELAY / O_NONBLOCK (same function) - Enables nonblocking mode. When set read requests on the file can return immediately with a failure status
	//											if there is no input immediately available (instead of blocking). Likewise, write requests can also return
	//											immediately with a failure status if the output can't be written immediately.
	//
	//	O_NOCTTY - When set and path identifies a terminal device, open() shall not cause the terminal device to become the controlling terminal for the process.
	uart0_filestream = open("/dev/serial0", O_RDWR | O_NOCTTY | O_NDELAY);		//Open in non blocking read/write mode
	if (uart0_filestream == -1)
	{
		//ERROR - CAN'T OPEN SERIAL PORT
		printf("Error - Unable to open UART.  Ensure it is not in use by another application\n");
	}
	
	//CONFIGURE THE UART
	//The flags (defined in /usr/include/termios.h - see http://pubs.opengroup.org/onlinepubs/007908799/xsh/termios.h.html):
	//	Baud rate:- B1200, B2400, B4800, B9600, B19200, B38400, B57600, B115200, B230400, B460800, B500000, B576000, B921600, B1000000, B1152000, B1500000, B2000000, B2500000, B3000000, B3500000, B4000000
	//	CSIZE:- CS5, CS6, CS7, CS8
	//	CLOCAL - Ignore modem status lines
	//	CREAD - Enable receiver
	//	IGNPAR = Ignore characters with parity errors
	//	ICRNL - Map CR to NL on input (Use for ASCII comms where you want to auto correct end of line characters - don't use for bianry comms!)
	//	PARENB - Parity enable
	//	PARODD - Odd parity (else even)
	struct termios options;
	tcgetattr(uart0_filestream, &options);
	options.c_cflag = B115200 | CS8 | CLOCAL | CREAD;		//<Set baud rate
	options.c_iflag = IGNPAR;
	options.c_oflag = 0;
	options.c_lflag = 0;
	tcflush(uart0_filestream, TCIFLUSH);
	tcsetattr(uart0_filestream, TCSANOW, &options);
	
	
	
	
	char FormattedPayload[100]; 
	
	  // Turn off blocking for reads, use (fd, F_SETFL, FNDELAY) if you want that
  //fcntl(uart0_filestream, F_SETFL, 0);

  // Write to the port
  //int n = printf( uart0_filestream, "ATD%s;\r\n", DialerEntry);
  printf( FormattedPayload, "ATD%s;\r\n", DialerEntry);
  int n = write (uart0_filestream, FormattedPayload, 100);
  write(1, FormattedPayload,100);
  if (n < 0) {
    perror("Write failed - ");
    return -1;
  }
	
	
	
	
	//----- TX BYTES -----
//	unsigned char tx_buffer[20];
//	unsigned char *p_tx_buffer;
	
//	p_tx_buffer = &tx_buffer[0];
//	*p_tx_buffer++ = 'H';
//	*p_tx_buffer++ = 'e';
//	*p_tx_buffer++ = 'l';
//	*p_tx_buffer++ = 'l';
//	*p_tx_buffer++ = 'o';
	
//	if (uart0_filestream != -1)
//	{
//		int count = write(uart0_filestream, &tx_buffer[0], (p_tx_buffer - &tx_buffer[0]));		//Filestream, bytes to write, number of bytes to write
//		if (count < 0)
//		{
//			printf("UART TX error\n");
//		}
//	}
	

 	GtkWidget *GtkMessageDialogEndCall = gtk_message_dialog_new( GTK_WINDOW(GtkWidgetWindow), GTK_DIALOG_MODAL, GTK_MESSAGE_INFO, GTK_BUTTONS_OK, "Attempting to place call...");

    gtk_message_dialog_format_secondary_text( GTK_MESSAGE_DIALOG(GtkMessageDialogEndCall), "Click Ok to hang up.");

    int response = gtk_dialog_run(GTK_DIALOG(GtkMessageDialogEndCall));

    printf("response was %d (OK=%d, DELETE_EVENT=%d)\n", response, GTK_RESPONSE_OK, GTK_RESPONSE_DELETE_EVENT);

	gtk_widget_destroy(GtkMessageDialogEndCall);
	
	
	
	
	
	  printf( FormattedPayload, "AT+CVHU=0\r\n", DialerEntry);
  n = write (uart0_filestream, FormattedPayload, 100);
  if (n < 0) {
    perror("Write failed - ");
    return -1;
  }
  
  
  
  
  
    printf( FormattedPayload, "ATH\r\n", DialerEntry);
  n = write (uart0_filestream, FormattedPayload, 100);
  if (n < 0) {
    perror("Write failed - ");
    return -1;
  }
	
	
	
	//char * paramsList2[] = {"/bin/bash", "-c", "printf \"AT+CVHU=0\r\n\" > /dev/serial0",NULL};
	//execv ("/bin/bash", paramsList2);
	
	//char * paramsList3[] = {"/bin/bash", "-c", "printf \"ATH\r\n\" > /dev/serial0",NULL};
	//execv ("/bin/bash", paramsList3);
	
	//DialerEntry[DialerIndex] = 0;

	//while (DialerIndex > 0) {
	//	DialerIndex--;
	//	DialerEntry[DialerIndex] = 0;
	//}
	//gtk_entry_set_text( GTK_ENTRY(GtkWidgetEntry), DialerEntry );
	
	//----- CLOSE THE UART -----
	close(uart0_filestream);
	
} // End ClickedCall
