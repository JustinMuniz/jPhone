CC=gcc
CFLAGS=-I.

make: main.c
	$(CC) -o jdialer main.c -Wall `pkg-config --cflags --libs gtk+-3.0` -export-dynamic