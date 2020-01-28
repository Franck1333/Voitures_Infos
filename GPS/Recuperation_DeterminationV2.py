#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#AIDES:
#https://www.raspberrypi.org/forums/viewtopic.php?t=227664
#https://github.com/Knio/pynmea2

#---------------------Blibliotheques_du_Programme---------------------
import serial
import time
import os
import sys

import requests             #Lib permettant de faire des requetes HTTP(s) via python3
import json                 #Lib permettant de manipuler les informations reçu sous formats JSON
import pynmea2              #Lib permettant de manipuler les informations GPS avec le protocole NMEA
#---------------------Blibliotheques_du_Programme---------------------
global ser
ser = serial.Serial("/dev/ttyACM0",4800, 8, 'N', 1, timeout=1)   #Open Serial port Configure le Recepteur G.P.S 

def Read_GPSStick_GPRMC():
     while True:                                                 #Boucle Infinie (Tant que Vrai reste Vrai,)
          data = ser.readline()                                  #On recupere les informations en provenance de la liaison serie USB
          data = data.decode("utf-8","ignore")                   #On convertis les donnees binaires en donnees UTF-8 (str)

          #if sys.version_info[0] == 3:                          #Si dans la trame nous trouvons des informations non importante
          #   data = data.decode("utf-8","ignore")               #On convertis les donnees binaires en donnees UTF-8 (str)
          #   print(data)                                        #On les affiches dans la console

          if data[0:6] == '$GPRMC':                              #Si dans la trame NMEA on trouve un string ayant pour valeur '$GPRMC'
             print("\n")                                         #On saute une ligne
             print("Trame NMEA:GPRMC")                           #On affiche un message dans la console
             print(data)                                         #On affiche les donnees exploitable reçu
             return data                                         #On retourne les informations obtenue pour une utilisations utltérieur
     
def Obtention_GPRMC_Unique():   #Cette fonction permet d'obtenir les informations NMEA en provenance du Stick USB GPS et de les converir en donnée exploitable via PyNMEA2, Version Lancement unique
    try:                                                                   #Gestion d'erreur
        data = Read_GPSStick_GPRMC()                                       #Enregistrement des informations en provenance de la cle USB GPS
        print(data)                                                        #Affichage des informations recu par la cle USB GPS

        msg = pynmea2.parse(data)                                          #Traitement et Enregistrement des trames NMEA via PyNMEA2
        
        print(msg.lat +" "+ msg.lat_dir +" "+ msg.lon +" "+ msg.lon_dir)   #Affichage dans la console des informations utiles

        determine_Voiture(msg.latitude,msg.longitude)                      #Reverse Geocoding des informations traitee par PyNMEA2

    except TypeError:                                                      #Gestion d'erreur, Si il y a une erreur de type au niveau de la variable 'msg'
        msg = "Signal GPS Perdue, GPS Signal Lost, TypeError"              #Alors, cette valeurs String sera enregistrer dans 'msg'
        print(msg)                                                         #Affichage de l'erreur sera effectuer dans la console
    return msg                                                             #Si il y a ou non une erreur, alors on retourne l'information pour une utilisation ulterieur

def Obtention_GPRMC_Continue(): #Cette fonction permet d'obtenir les informations NMEA en provenance du Stick USB GPS et de les converir en donnée exploitable via PyNMEA2, Version Lancement repeter
    while True:                                                                                     #Boucle Infinie (Tant que Vrai reste Vrai,)
        data = ser.readline()                                                                       #On recupere les informations en provenance de la liaison serie USB

        if sys.version_info[0] == 3:                                                                #Si dans la trame nous trouvons des informations non importante
           data = data.decode("utf-8","ignore")                                                     #On convertis les donnees binaires en donnees UTF-8 (str)
           #print(data)                                                                             #Affichage de 'data' dans la console
           msg = "Nan,Nope"                                                                         #Si il y a une erreur, cette valeur sera prise en compte avec son Str
               
        if data[0:6] == '$GPRMC':                                                                   #Si dans la trame NMEA on trouve un string ayant pour valeur '$GPRMC'
           print(data)                                                                              #On affiche les donnees exploitable reçu
           msg = pynmea2.parse(data)                                                                #Traitement et Enregistrement des trames NMEA via PyNMEA2
           print(str(msg.latitude) +" "+ msg.lat_dir +" "+ str(msg.longitude) +" "+ msg.lon_dir)    #Affichage dans la console des informations utiles

           determine_Voiture(msg.latitude,msg.longitude)                                            #Reverse Geocoding des informations traitee par PyNMEA2
           
    return msg                                                                                      #Si il y a ou non une erreur, alors on retourne l'information pour une utilisation ulterieur

    
def determine_Voiture(Decimal_latitude,Decimal_longitude):  #Cette fonction permet de determiner la position GPS avec leurs dénominations officiel      
    try:
        send_url = "http://photon.komoot.de/reverse?lon="+str(Decimal_longitude)+"&lat="+str(Decimal_latitude)  #Requete http pour obtenir les informations geographique concernant une position GPS
        r = requests.get(send_url)
        j = json.loads(r.text)                                                                                  #Enregistrement des informations GPS sous format JSON

        #print("\n")
        #print(j)

        Ville =         j['features'][0]['properties']['city']                       #Enregistrement de la Ville
        Numero_Maison = j['features'][0]['properties']['housenumber']                #Enregistrement du Numéro de Rue
        Rue =           j['features'][0]['properties']['street']                     #Enregistrement de la Rue
        Region =        j['features'][0]['properties']['state']                      #Enregistrement de la Region
        Code_Postal =   j['features'][0]['properties']['postcode']                   #Enregistrement du Code Postal
        Pays =          j['features'][0]['properties']['country']                    #Enregistrement du Pays

        print(Ville+" "+Numero_Maison+" "+Rue+" "+Region+" "+Code_Postal+" "+Pays)   #Affichage des informations pour debug si problèmes, il y a

    except KeyError:
        Ville =         "Signal GPS Perdue"                                          #Enregistrement dans l'emplacement 'Ville' d'une valeur reportant une erreur en Francais                      
        Numero_Maison = "GPS Signal Lost"                                            #Enregistrement dans l'emplacement 'Numero_Maison' d'une valeur reportant une erreur en Anglais
        Rue =           " "                                         
        Region =        " "                                        
        Code_Postal =   " "                                        
        Pays =          "KeyError"                                                   #Enregistrement dans l'emplacement 'Pays' d'une valeur reportant une erreur format Python                                    
        print(Ville+" "+Numero_Maison+" "+Rue+" "+Region+" "+Code_Postal+" "+Pays)

    return Ville,Numero_Maison,Rue,Region,Code_Postal,Pays                           #Si il y a ou non une erreur, alors on retourne l'information pour une utilisation ulterieur

if __name__ == "__main__":
    #Read_GPSStick_GPRMC()         #Cette fonction permet de lire les informations recu par le port serie de l'Ordinateur en provenance de la cle USB GPS
    Obtention_GPRMC_Unique()       #Cette fonction permet d'obtenir les informations NMEA en provenance du Stick USB GPS et de les converir en donnée exploitable via PyNMEA2, Version Lancement unique
    #Obtention_GPRMC_Continue()    #Cette fonction permet d'obtenir les informations NMEA en provenance du Stick USB GPS et de les converir en donnée exploitable via PyNMEA2, Version Lancement repeter
    #time.sleep(5)
