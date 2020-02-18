#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------------Blibliotheque_du_Programme---------------------
import json
import requests

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()

import sys
sys.path.append("/home/"+USERNAME+"/Voitures_Infos/GPS")  #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print(USERNAME)                                          #Test debug
from GPSoI import recuperation_coordonees_ip_V2
#---------------------Blibliotheque_du_Programme---------------------

def Ville_de_reference():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)
    Ville = j["records"][0]["fields"]["city"]
    print("Ville :"+Ville)
    return Ville

def Energies_Carburants():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    Ville = j["records"][0]["fields"]["city"]
    prix_sp_98 = j["records"][0]["fields"]["price_sp98"]
    prix_e10 = j["records"][0]["fields"]["price_e10"]
    prix_diesel = j["records"][0]["fields"]["price_gazole"]
    prix_gpl = j["records"][0]["fields"]["price_gplc"]

    print("Ville : "+Ville)
    print("prix_sp_98 : "+ str(prix_sp_98)+" €/L")
    print("prix_e10 : "+ str(prix_e10)+" €/L")
    print("prix_diesel : "+ str(prix_diesel)+" €/L")
    print("prix_gpl : "+str(prix_gpl)+" €/L")

    return Ville,prix_sp_98,prix_e10,prix_diesel,prix_gpl

def Energies_Carburants_GPSoI():
    try:
        city,postal  = recuperation_coordonees_ip_V2()

        send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp="+postal+"&timezone=Europe%2FParis"
        r = requests.get(send_url)
        j = json.loads(r.text)

        Ville = city
        prix_sp_98 = j["records"][0]["fields"]["price_sp98"]
        prix_e10 = j["records"][0]["fields"]["price_e10"]
        prix_diesel = j["records"][0]["fields"]["price_gazole"]
        prix_gpl = j["records"][0]["fields"]["price_gplc"]

        print("Ville : "+Ville)
        print("Code Postal: "+ str(postal))
        print("prix_sp_98 : "+ str(prix_sp_98)+" €/L")
        print("prix_e10 : "+ str(prix_e10)+" €/L")
        print("prix_diesel : "+ str(prix_diesel)+" €/L")
        print("prix_gpl : "+str(prix_gpl)+" €/L")

        Affichage_prix_sp_98 = "SP-98: "+str(prix_sp_98)+" €/L"
        Affichage_prix_e10 = "E10: "+str(prix_e10)+" €/L"
        Affichage_prix_diesel = "Diesel: "+str(prix_diesel)+" €/L"
        Affichage_prix_gpl = "GPL: "+str(prix_gpl)+" €/L"

    except KeyError:
        print("Code Erreur: KeyError, Il y a peut-etre pas de GPL ici ?")
        prix_gpl = 0.00
        
        print("Ville : "+Ville)
        print("Code Postal: "+ str(postal))
        print("prix_sp_98 : "+ str(prix_sp_98)+" €/L")
        print("prix_e10 : "+ str(prix_e10)+" €/L")
        print("prix_diesel : "+ str(prix_diesel)+" €/L")
        print("prix_gpl : "+str(prix_gpl)+" €/L")

        Affichage_Lieux = "Prix carburants sur "+Ville+","+str(postal)+": " 
        Affichage_prix_sp_98 = "SP-98: "+str(prix_sp_98)+" €/L"
        Affichage_prix_e10 = "E10: "+str(prix_e10)+" €/L"
        Affichage_prix_diesel = "Diesel: "+str(prix_diesel)+" €/L"
        Affichage_prix_gpl = "GPL: "+str(prix_gpl) +" €/L"
        
    return Affichage_Lieux,Affichage_prix_sp_98,Affichage_prix_e10,Affichage_prix_diesel,Affichage_prix_gpl

def Energie_essence98():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    prix_sp_98 = j["records"][0]["fields"]["price_sp98"]
    print("prix_sp_98 : "+ str(prix_sp_98)+" €/L")

    return prix_sp_98

def Energie_essence95():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    prix_e10 = j["records"][0]["fields"]["price_e10"]
    print("prix_e10 : "+ str(prix_e10)+" €/L")

    return prix_e10

def Energie_diesel():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    prix_diesel = j["records"][0]["fields"]["price_gazole"]
    print("prix_diesel : "+ str(prix_diesel)+" €/L")

    return prix_diesel
    
def Energie_gpl():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    prix_gpl = j["records"][0]["fields"]["price_gplc"]
    print("prix_gpl : "+str(prix_gpl)+" €/L")

    return prix_gpl

if __name__ == "__main__":
    #Ville_de_reference()
    #Energie_essence98()
    #Energie_essence95()
    #Energie_diesel()
    #Energie_gpl()
    #Energies_Carburants()
    Energies_Carburants_GPSoI()
