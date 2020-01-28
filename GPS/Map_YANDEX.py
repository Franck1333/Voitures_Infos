#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Aides : https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item
#Aides : http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
#Aides : https://staticmapmaker.com/yandex/

import getpass                                          #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                            #On enregistre le Nom de l'Utilisateur
import requests                                         #Lib permettant de faire des requetes HTTP(s) via python3
from tkinter import *
from Boussole import boussole                           #Obtention des Coordonnee GPS actuel
from ISS_locate import GPS_Now_ISS

def getMap():
    #---Service---#
    print('Telechargement de la Carte/Map .jpg')        #Message dans la Console
    latitude,dir_Latitude_Hemisphere,longitude,dir_Longitude_Hemisphere = boussole()

    url = "https://static-maps.yandex.ru/1.x/?lang=en-US&ll="+str(longitude)+","+str(latitude)+"&z=16&l=skl,map,trf&size=600,300&pt="+str(longitude)+","+str(latitude)+",flag"  #URL utilise pour obtenir la carte 
    #Ce service de MAP STATIC ce nomme YANDEX
    #Nous l'utilisons de cette facon : https://static-maps.yandex.ru/1.x/?lang=en-US&ll=LONGITUDE,LATITUDE&z=13&l=skl,map,trf&size=600,300&pt=LONGITUDE,LATITUDE,flag
    #Telechargement de l'image resultant de la requete
    response = requests.get(url)
    with open('/home/'+USERNAME+'/Voitures_Infos/GPS/MAP_downloads/map.jpg', 'wb') as f:
        f.write(response.content)
        print('Reception terminer de la Carte/Map .jpg')
    #---Service---#

def getMap_ISS():
    #---Service---#
    print('Telechargement de la Carte/Map .jpg #ISS')   #Message dans la Console

    tk_lisible_apparition,tk_ISS_latitude,tk_ISS_longitude,tk_Emplacement_ISS,latitude,longitude = GPS_Now_ISS()

    #print(longitude,latitude)
    url = "https://static-maps.yandex.ru/1.x/?lang=en-US&ll="+str(longitude)+","+str(latitude)+"&z=8&l=skl,map,trf&size=600,300&pt="+str(longitude)+","+str(latitude)+",flag"  #URL utilise pour obtenir la carte 
    response = requests.get(url)
    with open('/home/'+USERNAME+'/Voitures_Infos/GPS/MAP_downloads/map_ISS.jpg', 'wb') as f:
        f.write(response.content)
        print('Reception terminer de la Carte/Map .jpg')    #Telechargement de l'image resultant de la requete
    #---Service---#

###################
#Interface de Test#
###################
def getMapInterface():
    #---Interface---#

    #import Tkinter as tk
    #tk.NoDefaultRoot

    print('Affichage de la Carte/Map .jpg Telechargee')     #Message dans la Console

    fenetre = Tk()

    #Zone d'affichage
    EnveloppeMAP = LabelFrame(fenetre, text="La Position Geographique de l'ISS par rapport à la Terre", padx=5, pady=5)     #Création d'une "Zone Frame" à Label
    EnveloppeMAP.pack(fill="both", expand="no")                                                                             #Position de la "Zone Frame" à Label dans la fenêtre

    canvas = Canvas(EnveloppeMAP,width=600, height=300, bg='black')                                                         #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)

    canvas.pack(expand=NO, fill=None)                                                                                       #Placement du CANVAS de l'espace

    MAPjpg = PhotoImage(file='/home/'+USERNAME+'/Voitures_Infos/GPS/MAP_downloads/map_ISS.jpg')                             #Chargement de la MAP

    canvas.create_image(0,0,image=MAPjpg,anchor=NW)                                                                         #Integration de la MAP

    Button(fenetre, text="Fermer", command=fenetre.destroy).pack()                                                          #Bouton de Fermeture du Programme

    fenetre.mainloop()                                                                                                      #Lancement du Programme Principal
    #---interface---#

if __name__ == "__main__":
    getMap()
    getMap_ISS()
    getMapInterface()   
