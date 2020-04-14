#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------
import os
import sys
import datetime
import time
#---------------

def Conso_Theorique(Volume_Reservoir,Distance_Trajet):
    #Calcul:
    #V = Volume d'un Reservoir
    #D = Distance d'un trajet effectuer (en Km)
    #V*100/D = Conso_Instant (en Litre) sur 100Km

    Resultats_Conso_sur_100Km = Volume_Reservoir*100/Distance_Trajet
    Affichage_Resultats_Conso_sur_100Km = str(Resultats_Conso_sur_100Km)+" L/100Km"
    print(Affichage_Resultats_Conso_sur_100Km)

    return Affichage_Resultats_Conso_sur_100Km

def Prix_essence_consommee(Conso_litre_carburant,Prix_du_carburant):
    #Calculs:
    #C = Consommation en litre (L)
    #P = Prix du carburant (€)
    #RSLT = Prix de l'essence consommee au total en (€)
    #C*P = RSLT(€)

    Total_Prix_essence = Conso_litre_carburant*Prix_du_carburant
    Affichage_Total_Prix_essence = str(Total_Prix_essence)+" €"
    print(Affichage_Total_Prix_essence)

    return Affichage_Total_Prix_essence    

if __name__ == "__main__":
    Conso_Theorique(20,200)
    Prix_essence_consommee(7,1.519)
