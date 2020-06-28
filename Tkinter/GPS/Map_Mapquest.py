#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Aides : https://staticmapmaker.com/yandex/
#Aides : https://developer.mapquest.com/documentation/open/static-map-api/v4/place-map/get/

import getpass                                          #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                            #On enregistre le Nom de l'Utilisateur
import requests                                         #Lib permettant de faire des requetes HTTP(s) via python3
from tkinter import *

def getMapAdresse(Adresse,Zoom):
    #---Service---#
    print('Telechargement de la Carte/Map .png')        #Message dans la Console

    #PARAMETRE CHANGEABLE:
    #Adresse -> Saisir l'adresse a rechercher avec les noms des emplacements officiels.
    #Zoom -> Saisir l'agrandissement dans l'image d'une valeur allant de 1 a 18 maximum.
    url = "https://open.mapquestapi.com/staticmap/v4/getplacemap?key=aeXE6bajRzVQ3eCy69XlAz7wVXPfp4zJ&location="+str(Adresse)+"&size=600,300&imagetype=png&zoom="+str(Zoom)+"&showicon=red_1-1"  #URL utilise pour obtenir la carte 

    #Ce service de MAP STATIC ce nomme MapQuest
    #Nous l'utilisons de cette facon : https://open.mapquestapi.com/staticmap/v4/getplacemap?key=KEY&location=Angers,France&size=600,300&imagetype=png&zoom=18&showicon=red_1-1
    #Telechargement de l'image resultant de la requete
    response = requests.get(url)
    with open('/home/'+USERNAME+'/Voitures_Infos/Tkinter/GPS/MAP_downloads/map_addresse.png', 'wb') as f:
        f.write(response.content)
        print('Reception terminer de la Carte/Map .png')
    #---Service---#

###################
#Interface de Test#
###################
def getMapInterface():
    #---Interface---#

    #import Tkinter as tk
    #tk.NoDefaultRoot

    print('Affichage de la Carte/Map .png Telechargee')     #Message dans la Console

    fenetre = Tk()

    #Zone d'affichage
    EnveloppeMAP = LabelFrame(fenetre, text="Resultat de votre recherche: ", padx=5, pady=5)                                #Création d'une "Zone Frame" à Label
    EnveloppeMAP.pack(fill="both", expand="no")                                                                             #Position de la "Zone Frame" à Label dans la fenêtre

    canvas = Canvas(EnveloppeMAP,width=600, height=300, bg='black')                                                         #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)

    canvas.pack(expand=NO, fill=None)                                                                                       #Placement du CANVAS de l'espace

    MAPjpg = PhotoImage(file='/home/'+USERNAME+'/Voitures_Infos/Tkinter/GPS/MAP_downloads/map_addresse.png')                #Chargement de la MAP

    canvas.create_image(0,0,image=MAPjpg,anchor=NW)                                                                         #Integration de la MAP

    Button(fenetre, text="Fermer", command=fenetre.destroy).pack()                                                          #Bouton de Fermeture du Programme

    fenetre.mainloop()                                                                                                      #Lancement du Programme Principal
    #---interface---#

    
if __name__ == "__main__":
    getMapAdresse("Chemille-En-Anjou", "9")
    getMapInterface()
