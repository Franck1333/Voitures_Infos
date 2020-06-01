#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ROCHAT_FRANCK
#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date
#---------------------------------------Importante LIB---------------------------------------
#------------------------------------------------------------------------------#Affichage du Temps HEURES/MINUTES/SECONDES
def temps_actuel():   
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    #print(("Voici l'heure:",system_time))
    print(system_time)  #This print is used as a 'return' for NodeJS app with 'child_process' framework
    return system_time
    #-- FIN -- Heure,Minute,Seconde
#---------------------------------------------

if __name__ == "__main__":
    temps_actuel()
