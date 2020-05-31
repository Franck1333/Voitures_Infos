#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#AIDES:
##https://www.raspberrypi.org/forums/viewtopic.php?t=210680
#http://aprs.gids.nl/nmea/#gsv

#---------------------Blibliotheques_du_Programme---------------------
import serial
import time
import os
import sys

import pynmea2        #Lib permettant de manipuler les informations GPS avec le protocole NMEA
#---------------------Blibliotheques_du_Programme---------------------

#--------------------------------Local_LIB------------------------
from Recuperation_DeterminationV2 import Obtention_GPRMC
#--------------------------------Local_LIB------------------------

def Etat_connection_GPS():
    #Vue que je n'ai pas réussie a connaitre le SNR sur la trame NMEA:$GPGSV en utilisant le parser PyNMEA2
    #Le but desormais est de connaitre l'état de la validite de la trame NMEA:$GPRMC

    msg = Obtention_GPRMC()

    if msg.status == 'A':
        etat_gps = True
        Affichage_etat_gps = 'GPS: OK'
    else:
        etat_gps = False
        Affichage_etat_gps = 'GPS: Err'

    print(msg.status)
    print(etat_gps)
    print(Affichage_etat_gps)

    return Affichage_etat_gps

if __name__ == "__main__":
    Etat_connection_GPS()
