#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#---------------------Blibliotheques_du_Programme---------------------
import serial
import time
import os
import sys

from Recuperation_DeterminationV2 import Read_GPSStick_GPRMC    #Cette fonction permet de recuperer les informations envoyer depuis la cle USB GPS
import unicodedata                                              #Cette blibliothèque permet de travailler avec du contenue contenant des accents
import pynmea2                                                  #Lib permettant de manipuler les informations GPS avec le protocole NMEA
#---------------------Blibliotheques_du_Programme---------------------

def boussole():
    dataGPS = Read_GPSStick_GPRMC()                                                                     #Enregistrement des informations en provenance de la cle USB GPS
    #print(dataGPS)                                                                                     #Affichage des informations recu par la cle USB GPS
    msg = pynmea2.parse(dataGPS)                                                                        #Traitement et Enregistrement des trames NMEA via PyNMEA2

    latitude = msg.latitude                                                                             #La Latitude recu par le GPS est convertis en Degree Decimal par PyNMEA2 puis enregistrer
    latitude_Hemisphere = msg.lat_dir                                                                   #Enregistrement de la direction de la Latitude

    Longitude = msg.longitude                                                                           #La Longitude recu par le GPS est convertis en Degree Decimal par PyNMEA2 puis enregistrer
    Longitude_Hemisphere = msg.lon_dir                                                                  #Enregistrement de la direction de la Longitude

    print(str(latitude) +" "+ latitude_Hemisphere +" "+ str(Longitude) +" "+ Longitude_Hemisphere)      #Affichage dans la console des informations utiles    
    return latitude,latitude_Hemisphere,Longitude,Longitude_Hemisphere                                  #Retourne toutes les valeurs obtenues

if __name__ == "__main__":
    boussole()      #Programme principal de la Boussole Numérique (TEXTUELLE)
