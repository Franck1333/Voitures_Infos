#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#AIDES:
#http://ozzmaker.com/berrygps-setup-guide-raspberry-pi/
#http://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/

#---------------------Blibliotheque_du_Programme---------------------
import serial
import time
import os
import sys

import requests             #Lib permettant de faire des requetes HTTP(s) via python3
import json                 #Lib permettant de manipuler les informations reçu sous formats JSON
import pynmea2              #Lib permettant de manipuler les informations GPS avec le protocole NMEA
#---------------------Blibliotheque_du_Programme---------------------


from gps import *
import time
    
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
print ('latitude\tlongitude\ttime utc\t\t\taltitude\tepv\tept\tspeed\tclimb') # '\t' = TAB to try and output the data in columns.
   
try:
 
 
    while True:
        report = gpsd.next() #
        if report['class'] == 'TPV':
             
            print  (report,'lat',0.0),"\t",
            print  (report,'lon',0.0),"\t",
            print (report,'time',''),"\t",
            print  (report,'alt','nan'),"\t\t",
            print  (report,'epv','nan'),"\t",
            print  (report,'ept','nan'),"\t",
            print  (report,'speed','nan'),"\t",
            print (report,'climb','nan'),"\t"
 
        time.sleep(1) 
 
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("Done.\nExiting.")
