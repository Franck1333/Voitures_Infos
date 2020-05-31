#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#AIDES: https://gist.github.com/taylor224/516de7dd0b707bc0b1b3
#AIDES: https://wifi.readthedocs.io/en/latest/scanning.html#connecting-to-a-network  \\La doc n'est pas tres claire :O.

import os
import sys
import datetime
import time

import wifi                             #Lib Wifi
from wifi import Cell,Scheme


def Etat_Wifi():
    wifilist = []                       #On créer une liste des HotSpot Wi-Fi scanner
    infoList = []                       #On créer une liste où les informations de qualite du Signal des HotSpot seront renseiger

    cells = wifi.Cell.all('wlan0')      #On obtient la taille pour la requete dans la boucle for

    for cell in cells:                  #On obtient les infos
        wifilist.append(cell)           #On les inscrit dans la liste wifilist
        infoList.append(cell.quality)   #On inscrit les informations de qualitee dans la liste infoList

    return wifilist[0],infoList[0]      #On retourne les infos pour le Hotspot auxquel l'utilisateur est connecter.

def Affichage_UI_Wifi():
    try:
        wifilist,infoList = Etat_Wifi()
        print("Wi-Fi: " + str(wifilist)+" " + str(infoList))
        Etat_Wifi_UI = "Wi-Fi: " + str(wifilist) +" " + str(infoList)
    except:
        Etat_Wifi_UI = "Wi-Fi: Non Connectée"
    return Etat_Wifi_UI

if __name__ == "__main__":
    #wifilist,infoList = Etat_Wifi()        #Obention des informations concernant la connectivité Wifi
    #print(wifilist)
    #print(infoList)
    Affichage_UI_Wifi()
