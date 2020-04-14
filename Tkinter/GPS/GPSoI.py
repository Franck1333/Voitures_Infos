#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#Aides: https://stackoverflow.com/questions/24906833/get-your-location-through-python
#Aides: https://github.com/Franck1333/GPS-Display/blob/master/Mon_Travail/Recuperation_Determination.py

import requests     #<-- Utilisation d'une Adresse URL Normalisée
import json         #<-- Permet l'expoitation de fichier en format JSON

#EXPLICATION --DEBUT--
#Ce Programme est utile pour determine la localisation de l'Adresse IP de l'utilisateur
#En revanche , ce programme n'indique pas la localisation exacte de l'utilisateur, dans ce cas elle sera imprécise!!!
#EXPLICATION --FIN--
#Programme GPSoI original modifier! (Exemplaire original disponible dans le repertoire 'Exemple du Projet')
#----------

def recuperation_coordonees_ip_V1():
    #API https://ipstack.com

    send_url = 'http://api.ipstack.com/check?access_key=b0e724b68c170a901019d01552425f1a&format=1'
    r = requests.get(send_url)          #Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)              #Chargement des données reçu dans le fichier en format JSON

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    city = j['city']
    ZIP = j['zip']
    continent_name = j['continent_name']
    #print("L'adresse IP a ete localiser ici:",city)
    #print("Le code postal:",ZIP)
    #Information Géographique --FIN--

    return city,ZIP,continent_name      #Retourne le nom du continent où est localiser l'adresse I.P
#----------

def recuperation_coordonees_ip_V2():
    #API https://ipinfo.io/json

    send_url = 'https://ipinfo.io/json'
    r = requests.get(send_url)          #Ouverture de L'URL pour l'utilisation de L'API
    j = json.loads(r.text)              #Chargement des données reçu dans le fichier en format JSON

    #Information Technique --DEBUT--
    ip = j['ip']
    print("Voici votre adresse I.P:", ip)
    #Information Technique --FIN--

    #Information Géographique --DEBUT--
    city = j['city']
    postal = j['postal']
    #print("L'adresse IP a ete localiser ici:",city)
    #print("Le code postal:",postal)
    #Information Géographique --FIN--

    return city,postal                  #Retourne le nom du continent où est localiser l'adresse I.P
#----------

if __name__ == "__main__":
    recuperation_coordonees_ip_V1()    #Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur.
    recuperation_coordonees_ip_V2()     #Fonctionnalité permettant d'Obtenir/Determiné les coordonées GPS correspondant à l'Adresse I.P de l'utilisateur , PROVENANT d'un autre service.
