#!/usr/bin/python3
#Recuperation_DeterminationV2.py, based on it
#https://www.raspberrypi.org/forums/viewtopic.php?t=227664
import sys
import pynmea2
import serial
ser = serial.Serial("/dev/ttyACM0",4800, 8, 'N', 1, timeout=1) 
while True:
     data = ser.readline()
     if sys.version_info[0] == 3:
        data = data.decode("utf-8","ignore")
     if data[0:6] == '$GPRMC':
        print(data)
