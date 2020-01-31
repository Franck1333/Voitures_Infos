#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#AIDES:
#https://www.raspberrypi.org/forums/viewtopic.php?t=210680
#https://forum.arduino.cc/index.php?topic=418337.0

#---------------------Blibliotheques_du_Programme---------------------
import serial
import time
import os
import sys

import pynmea2                                              #Lib permettant de manipuler les informations GPS avec le protocole NMEA

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME                                             #USERNAME en global pour etre utiliser plus tard dans le fichier
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur
sys.path.append("/home/"+USERNAME+"/Voitures_Infos/GPS")    #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil

from Recuperation_DeterminationV2 import Read_GPSStick_GPRMC
#---------------------Blibliotheques_du_Programme---------------------

def la_Vitesse_GPS():
    RMCdata = Read_GPSStick_GPRMC()                                             #On obtient la Trame NMEA venant du Stick USB GPS 
    RMCmsg = pynmea2.parse(RMCdata)                                             #Traitement et Enregistrement des trames NMEA via PyNMEA2

    #print(RMCmsg.spd_over_grnd)
    #kph =(int)(GPS.speed * 1.852);   // knots -> kph
    #mph =(int)(GPS.speed * 1.150779);// knots -> mph

    #Convertir les noeds en Kilometre par heure KMH
    KMH = float(RMCmsg.spd_over_grnd) * 1.852                                   #On convertis la valeur recue en Noeud en Kilometre Par Heure
    print("La vitesse de l'utilisateur: "+ str(KMH) + " Kilometre /h")          #On affiche le resultat dans la console
    Affichage_KMH = "Votre Vitesse : "+str(KMH)+" Km\h"

    return Affichage_KMH                                                        #On retourne la valeur pour une utilisation ulterieure (UI)

if __name__ == "__main__":
    la_Vitesse_GPS()    #Fonction permette d'obtenir la vitesse de l'utilisateur en Kilometre par heure.
