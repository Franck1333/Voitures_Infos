#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ROCHAT_FRANCK
#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from tkinter import *                                       #Blibliotheque permettant d'obtenir Tkinter(G.U.I)
from tkinter.messagebox import *                            #Blibliotheque permettant d'obtenir les boites de dialogues (G.U.I)
import tkinter.ttk                                          #Blibliotheque permettant de charger un composant Tkinter(G.U.I)

#from pydub import AudioSegment                             #Bibliotheque permettant de jouer des Sons et Jingles
#from pydub.playback import play                            #Bibliotheque permettant de jouer des Sons et Jingles
#---------------------------------------Importante LIB---------------------------------------

#-----------------------------------------------------Localisation de l'emplacement des fichiers necessaires-----------------------------------------------------
print("\n Bonjour/Bonsoir, ne pas faire fonctionner ce programme en utilisant les droits/commandes administrateur si l'utilisateur n'est pas l'Admin au quel cas le programme ne fonctionnera pas correctement. \n") #Information a lire dans la console

sys.path.append("/home/"+USERNAME+"/Voitures_Infos/Tkinter/Services")   #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print("User: "+USERNAME)                                               #Test debug
from Infos_Hardware import CPU_usage                                    #Obtention de l'utilisation du Processeur par le Systeme d'exploitation et ses programmes autour
from Infos_Hardware import CPU_temp                                     #Obtention de la Temperature du Processeur sur la carte mere
from Infos_Hardware import SoC_info                                     #Obtention des informations concernant le package CPU+GPU
from Infos_Hardware import MEM_info                                     #Obtention de l'utilisation de la Memoire Vive du Systeme
from Etat_Lien_WiFi import Affichage_UI_Wifi                            #Indication de l'état de la liaison Wi-Fi
from Vitesse_Utilisateur import la_Vitesse_GPS                          #Obtention par calcul de la vitesse de l'utilisateur en KM\h
from Services_Energies import Energies_Carburants_GPSoI                 #Obtention des différents prix des carburant en fonction de geocalisation global par IP de l'utilisateur

sys.path.append("/home/"+USERNAME+"/Voitures_Infos/Tkinter/GPS")        #On indique au systeme ou ce situe le repertoire "GPS" dans l'Appareil
from Etat_Signal_GPS import Etat_connection_GPS                         #Indication pour savoir si la liaison GPS est etablie ou non
from emergency_number import numero_urgence                             #Obtention des numéros d'urgence disponibles dans le continent de l'utilisateur
from Boussole import Affichage_boussole                                 #Obtention des coordonees GPS de l'utilisateur
from Meteo import main_meteo                                            #Obtention de la meteo au lieu localiser
from Recuperation_DeterminationV2 import Obtention_GPRMC_Unique         #Avec les coordonnees GPS, nous obtenons l'adresse physique de l'utilisateur simplement
from Map_YANDEX import getMap                                           #Obtention de la Carte sous forme d'une Image.JPG de la position GPS de l'Utilisateur
from Map_YANDEX import getMap_ISS                                       #Obtention de la Carte sous forme d'une Image.JPG de la position GPS de la Station Spacial International
from Map_Mapquest import getMapAdresse                                  #Obtention d'une carte sous forme d'une Image.PNG d'une recherche d'adresse precise
from ISS_locate import GPS_Now_ISS                                      #Obtention de la localisation de l'ISS en temps reel
from ISS_locate import GPS_Predict_ISS                                  #Obtention des passages visibles de l'ISS dans le ciel par rapporta la Position GPS de l'Utilisateur
#-----------------------------------------------------Localisation de l'emplacement des fichiers necessaires-----------------------------------------------------

#-------------Fenetre Maitre-------------
fenetre = Tk()              #Creation d'une Fenetre Maîtresse TK appeler "fenetre"
#-------------Fenetre Maitre-------------

#-------------------------------------------------------------------Contenue Fenetre Principale-------------------------------------------------------------------
#------------------------------------------------------------------------------#Affichage du Temps HEURES/MINUTES/SECONDES
def temps_actuel():   
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print(("Voici l'heure:",system_time))
    return system_time
    #-- FIN -- Heure,Minute,Seconde
#---------------------------------------------
status_temps_actuel = Label(fenetre, text=temps_actuel())                   #Affichage du Temps (Label)
status_temps_actuel.pack()                                                  #Pour obtenir un affichage dynamique , Il faut utiliser pack/grid de cette façon
#---------------------------------------------
def update_temps_actuel():                                                  #Fonctionnalité permettant de mettre à jour l'Heure en fonction du Temps Réel
    # On met à jour le temps actuel dans le champs text du Widget LABEL pour afficher l'heure
    status_temps_actuel["text"] = temps_actuel()
    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_temps_actuel)    
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def information_Materiel():
    #Obtention des Informations Materiel de l'Ordinateur
    global tk_UtilisationCPU
    global tk_tk_cputemp
    global tk_MemoireUtilise
    
    #--        
    UtilisationCPU = CPU_usage()                                                #Obtention du Niveau d'utilisation du Processeur.
    MemoireUtilise = MEM_info()                                                 #Obtention d'information par rapport à la Memoire Vive.
    tk_cputemp = CPU_temp()                                                     #Obtention de la Temperature du Package Processeur/GPU.
    mesure_voltage,memoire_processeur,memoire_gpu  = SoC_info()                 #Obtention d'information par rapport au Couple CPU/GPU.
    #--
    
    #--Affichage--
    EnveloppeInfoMateriel = LabelFrame(fenetre, text="Informations Relatives aux Matériels", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoMateriel.pack(fill="both", expand="no")                                                        #Position de la "Zone Frame" à Label dans la fenêtre
    tk_UtilisationCPU = Label(EnveloppeInfoMateriel, text=UtilisationCPU)                                       #Affichage de l'utilisation CPU
    tk_MemoireUtilise = Label(EnveloppeInfoMateriel, text=MemoireUtilise)                                       #Affichage de la Memoire utilise
    tk_tk_cputemp = Label(EnveloppeInfoMateriel, text=tk_cputemp)                                               #Affichage de la Temperture du CPUpackage
    tk_UtilisationCPU.pack()                                                                                    #Placement dans l'espace des informations
    tk_MemoireUtilise.pack()
    tk_tk_cputemp.pack()    
    #--Affichage--
    
def update_information_Materiel():
    #Mise a Jour des Informations a Propos du Materiel
    tk_UtilisationCPU["text"] = CPU_usage()
    tk_MemoireUtilise["text"] = MEM_info()
    tk_tk_cputemp["text"] = CPU_temp()    
    # Après une seconde , on met à jour le contenue text du LABEL
    fenetre.after(1000, update_information_Materiel)
#---
information_Materiel() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def information_Complementaire():
    #Etape-1bis On Declare les informations a mettre a jour
    #global tk_info_supp
    global connect_GPS_tk
    global connect_WIFI_tk
    
    #Etape-2 On recupere les informations a afficher
    #INFOS_SUPP = "Aucune Informations Supp. à affichée pour le moment."
    connect_GPS = Etat_connection_GPS()
    connect_WIFI= Affichage_UI_Wifi()

    #Etape-3 On fait la mise en page des Informations receptionner
    #Zone d'affichage
    EnveloppeInfoComplementaire = LabelFrame(fenetre, text="Informations Complémentaires", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoComplementaire.pack(fill="both", expand="no")

    #tk_info_supp = Label(EnveloppeInfoComplementaire, text= INFOS_SUPP)
    connect_GPS_tk = Label(EnveloppeInfoComplementaire, text= connect_GPS)
    connect_WIFI_tk = Label(EnveloppeInfoComplementaire, text= connect_WIFI)

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    #tk_info_supp.pack()
    connect_GPS_tk.pack()
    connect_WIFI_tk.pack()
    
def update_information_Complementaire():
    #Mise à Jour des Informations reçues
    #tk_info_supp["text"] = INFOS_SUPP
    connect_GPS_tk["text"] = Etat_connection_GPS()
    connect_WIFI_tk["text"] = Affichage_UI_Wifi()
    
    # Après x minutes , on met à jour le contenue text du LABEL
    fenetre.after(2048, update_information_Complementaire)
#---
information_Complementaire() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Informations_GPS():    
    print("Informations_GPS")
    
    #Etape-1 On Declare la fenetre
    global Info_GPS
    Info_GPS = Toplevel()

    #Etape-2 On recupere les informations a afficher
    Numero_urgence_continental =    numero_urgence()
    Boussole_Numerique =    Affichage_boussole()
    Localisation =  Obtention_GPRMC_Unique()
    Vitesse_user =  la_Vitesse_GPS() 

    #Etape-3 On fait la mise en page des Informations receptionner
    #Zone d'affichage
    EnveloppeInfo_GPS = LabelFrame(Info_GPS, text="Informations GPS Basique", padx=5, pady=5)       #Création d'une "Zone Frame" à Label
    EnveloppeInfo_GPS.pack(fill="both", expand="no")                                                #Position de la "Zone Frame" à Label dans la fenêtre
    Numero_urgence_continental_tk = Label(EnveloppeInfo_GPS, text= Numero_urgence_continental)    
    Boussole_Numerique_tk = Label(EnveloppeInfo_GPS, text= Boussole_Numerique)

    EnveloppeInfo_GPS_Complete = LabelFrame(Info_GPS, text="Informations GPS Complète", padx=5, pady=5)         #Création d'une "Zone Frame" à Label
    EnveloppeInfo_GPS_Complete.pack(fill="both", expand="no")                                                   #Position de la "Zone Frame" à Label dans la fenêtre
    Localisation_tk = Label(EnveloppeInfo_GPS_Complete, text= Localisation)

    EnveloppeInfo_GPS_Conduite = LabelFrame(Info_GPS, text="Informations GPS Conduite", padx=5, pady=5)         #Création d'une "Zone Frame" à Label
    EnveloppeInfo_GPS_Conduite.pack(fill="both", expand="no")                                                   #Position de la "Zone Frame" à Label dans la fenêtre
    Vitesse_user_tk = Label(EnveloppeInfo_GPS_Conduite, text= Vitesse_user)
    Conso_user_tk = Label(EnveloppeInfo_GPS_Conduite, text="*Estimation Conso Carburant: 5L/100 Km*")

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    Numero_urgence_continental_tk.pack()
    Boussole_Numerique_tk.pack()
    Localisation_tk.pack()
    Vitesse_user_tk.pack()
    Conso_user_tk.pack() #A concevoir le service.
    
    #Etape-5 Effectuer les mises a jours des Informations recues
    def update_Informations_GPS():
        print("update_Informations_GPS")
        #Mise à Jour des Informations reçues par recuperation des informations
        #Numero_urgence_continental_tk["text"] = numero_urgence()
        Boussole_Numerique_tk["text"] = Affichage_boussole()
        Localisation_tk["text"] = Obtention_GPRMC_Unique()
        Vitesse_user_tk["text"] = la_Vitesse_GPS()
        
        # Après x temps , on met à jour le contenue text du LABEL
        fenetre.after(3096, update_Informations_GPS)
        
    #Etape-5(Bis) Lancer les mises a jours des informations recues
    update_Informations_GPS()

    #---MAP YANDEX---
    def Show_MAP():
        #Dans cette fonctionnalitee nous allons obtenir une carte ou ce situe l'utilisateur du Logiciel.
        global Show_YANDEXMAP
        #global MAPjpg
        Show_YANDEXMAP = Toplevel()
        #Execution du script Python permettant la recuperation de la carte et Recuperation de l'emplacement de la carte dans l'ordinateur
        getMap()
        #Zone d'affichage
        EnveloppeMAP = LabelFrame(Show_YANDEXMAP, text="Votre Position Geographique", padx=5, pady=5)       #Création d'une "Zone Frame" à Label
        EnveloppeMAP.pack(fill="both", expand="no")                                                         #Position de la "Zone Frame" à Label dans la fenêtre
        canvas = Canvas(EnveloppeMAP,width=600, height=300, bg='black')                                     #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)
        canvas.pack(expand=NO, fill=None)                                                                   #Placement du CANVAS de l'espace
        MAPjpg = PhotoImage(file="/home/"+USERNAME+"/Voitures_Infos/Tkinter/GPS/MAP_downloads/map.jpg")     #Chargement de la MAP
        canvas.file = MAPjpg                                                                                #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
        image_on_canvas = canvas.create_image(0,0,image=MAPjpg , anchor=NW)                                 #Integration de la MAP
        #--UPDATE--
        def update_refresh_Show_MAP():
            print("Mise a Jour de la Cartographie Geographique")                                            #Message dans la Console
            getMap()                                                                                        #Obtention d'une Nouvelle Cartographie
            MAPjpg = PhotoImage(file="/home/"+USERNAME+"/Voitures_Infos/Tkinter/GPS/MAP_downloads/map.jpg") #Chargement de la MAP
            canvas.file = MAPjpg                                                                            #REFERENCE A GARDER pour pas perdre Tkinter sinon sans cette Reference , il perd l'image (Voir Explication ici: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
            canvas.itemconfig(image_on_canvas,image= MAPjpg)                                                #Permet la mise a jour de l'image
             # Après X secondes , on met à jour le contenue text du LABEL
            Show_YANDEXMAP.after(3000, update_refresh_Show_MAP)
        #--UPDATE--
        update_refresh_Show_MAP()   #Fonctionnalité permettant de mettre à jours dans l'interface la Carte Geographique de la position de l'Utilisateur
        Button(Show_YANDEXMAP, text="Fermer", command=Show_YANDEXMAP.destroy).pack()  #Bouton de Fermeture de la Fenetre actuelle        
    #---MAP YANDEX---  

    #Etape-6 Bouton(s)
    Button(Info_GPS, text="Yandex Map", command=Show_MAP).pack()  #Bouton d'affichage de la Map by Yandex
    Button(Info_GPS, text="Fermer", command=Info_GPS.destroy).pack()  #Bouton de Fermeture de la Fenetre actuelle
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def Recherche_Adresse():
    print("Recherche_Adresse")

    #Etape-1 On Declare la fenetre
    global Map_Adresse
    Map_Adresse = Toplevel()

    #Etape-2 On recupere les informations a afficher & 3 On fait la mise en page des Informations receptionner
    #Zone d'affichage

    EnveloppeMap_Adresse = LabelFrame(Map_Adresse, text="Recherche Satellite", padx=5, pady=5)                  #Création d'une "Zone Frame" à Label
    EnveloppeMap_Adresse.pack(fill="both", expand="no")                                                         #Position de la "Zone Frame" à Label dans la fenêtre

    Consigne_Saisie_Adresse_1 = Label(EnveloppeMap_Adresse, text= "Saisissez l'Adresse à cartographier: ")      #Affichage des consignes d'utilisations
    Consigne_Saisie_Adresse_2 = Label(EnveloppeMap_Adresse, text= "Ex: Rue,Code Postal,Ville (Nom Officiel) et/ou Pays.")

    textBox_Addresse=Text(EnveloppeMap_Adresse,height=1, width=30)                                              #Affichage de la boite a texte
    
    Consigne_Choix_Zoom = Label(EnveloppeMap_Adresse, text= "Selectionnez le Zoom de la carte (1 à 18).")
    spinbox_Zoom = Spinbox(EnveloppeMap_Adresse, from_=1, to=18)                                                #Affichage de l'outil permettant de selectionner certaine valeurs numerique

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    Consigne_Saisie_Adresse_1.pack()                                                                            #Placement dans l'espace des Informations
    Consigne_Saisie_Adresse_2.pack()
    textBox_Addresse.pack()                                                                                     #Placement dans l'espace de la bare de saisie
    Consigne_Choix_Zoom.pack()
    spinbox_Zoom.pack()                                                                                         #Placement dans l'espace de l'outil specifique au choix d'une valeurs numerique
    
    #Etape-6 Bouton(s)
    Button(Map_Adresse, height=1, width=13, text="Go!",command=lambda: recuperation_input_Addresse_Zoom()).pack()  #Affichage et Positionnement automatique du Bouton d'envoie de la valeur contenue dans la boite a texte
    Button(Map_Adresse, text="Fermer", command=Map_Adresse.destroy).pack()                                         #Bouton de Fermeture de la Fenetre actuelle

    def recuperation_input_Addresse_Zoom():
        Adresse_Saisie = textBox_Addresse.get("1.0","end-1c")   #Recuperation de la Valeur saisie dans la boite a texte
        Zoom_choisi = spinbox_Zoom.get()                        #Recuperation de la Valeur saisie dans la Spinbox
        print(Adresse_Saisie,Zoom_choisi)                       #Affichage de cette valeur dans la console
        getMapAdresse(Adresse_Saisie,Zoom_choisi)               #Telechargement de la cartographie vise par l'adresse saisie plutot
        Affichage_RechercheAdresse()                            #Affichage de la cartographie dans l'interface utilisateur

    def Affichage_RechercheAdresse():
        print("Affichage_RechercheAdresse")

        #Etape-1 On Declare la fenetre
        global Affichage_Map_Adresse
        Affichage_Map_Adresse = Toplevel()

        #Etape-2 On recupere les informations a afficher & 3 On fait la mise en page des Informations receptionner
        #Zone d'affichage
        EnveloppeAffichage_Map_Adresse = LabelFrame(Affichage_Map_Adresse, text="Voici la Carte: ", padx=5, pady=5)         #Création d'une "Zone Frame" à Label
        EnveloppeAffichage_Map_Adresse.pack(fill="both", expand="no")                                                       #Position de la "Zone Frame" à Label dans la fenêtre

        canvas = Canvas(EnveloppeAffichage_Map_Adresse,width=600, height=300, bg='black')                                   #Creer le CANVAS (Parent,Largeur,Hauteur,couleur de font)
        canvas.pack(expand=NO, fill=None)                                                                                   #Placement du CANVAS de l'espace
        MAPjpg = PhotoImage(file='/home/'+USERNAME+'/Voitures_Infos/Tkinter/GPS/MAP_downloads/map_addresse.png')            #Chargement de la MAP
        canvas.file = MAPjpg                                                                                                #REFERENCE A GARDER pour pas perdre Tkinter
        canvas.create_image(0,0,image=MAPjpg,anchor=NW)                                                                     #Integration de la MAP

        #Etape-6 Bouton(s)
        Button(Affichage_Map_Adresse, text="Fermer", command=Affichage_Map_Adresse.destroy).pack()                          #Affichage et positionnement automatique du bouton de fermeture de la fenetre d'Affichage de la cartographie
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def Meteo_Complete():
    print("Meteo_Complete")
    
    #Etape-1 On Declare la fenetre
    global Info_Meteo
    Info_Meteo = Toplevel()

    #Etape-2 On recupere les informations a afficher
    status_climat,climat_min,climat_now,climat_max,vitesse_du_vent,volume_de_neige,volume_de_pluie,pourcentage_humidite,couverture_de_nuage = main_meteo()
    
    #Etape-3 On fait la mise en page des Informations receptionner
    #Zone d'affichage
    EnveloppeInfo_Meteo = LabelFrame(Info_Meteo, text="Conditions Météorologiques", padx=5, pady=5)         #Création d'une "Zone Frame" à Label
    EnveloppeInfo_Meteo.pack(fill="both", expand="no")                                                      #Position de la "Zone Frame" à Label dans la fenêtre

    status_climat_tk = Label(EnveloppeInfo_Meteo, text= status_climat)    
    climat_min_tk = Label(EnveloppeInfo_Meteo, text= climat_min)
    climat_now_tk = Label(EnveloppeInfo_Meteo, text= climat_now)
    climat_max_tk = Label(EnveloppeInfo_Meteo, text= climat_max)
    vitesse_du_vent_tk = Label(EnveloppeInfo_Meteo, text= vitesse_du_vent)
    volume_de_neige_tk = Label(EnveloppeInfo_Meteo, text= volume_de_neige)
    pourcentage_humidite_tk = Label(EnveloppeInfo_Meteo, text= pourcentage_humidite)
    couverture_de_nuage_tk = Label(EnveloppeInfo_Meteo, text= couverture_de_nuage)

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    status_climat_tk.pack()
    climat_min_tk.pack()
    climat_now_tk.pack()
    climat_max_tk.pack()
    vitesse_du_vent_tk.pack()
    volume_de_neige_tk.pack()
    pourcentage_humidite_tk.pack()
    couverture_de_nuage_tk.pack()
    
    #Etape-5 Bouton(s)
    Button(Info_Meteo, text="Fermer", command=Info_Meteo.destroy).pack()  #Bouton de Fermeture de la Fenetre actuelle     
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Prix_du_Carburant():
    print("Prix du Carburant")

    #Etape-1 On Declare la fenetre
    global Info_Carbu
    Info_Carbu = Toplevel()

    #Etape-2 On recupere les informations a afficher
    Affichage_Lieux,Affichage_prix_sp_98,Affichage_prix_e10,Affichage_prix_diesel,Affichage_prix_gpl = Energies_Carburants_GPSoI()
    
    #Etape-3 On fait la mise en page des Informations receptionner
    #Zone d'affichage
    EnveloppeInfo_Carbu = LabelFrame(Info_Carbu, text="Tarifs des Carburants", padx=5, pady=5)      #Création d'une "Zone Frame" à Label
    EnveloppeInfo_Carbu.pack(fill="both", expand="no")                                              #Position de la "Zone Frame" à Label dans la fenêtre

    Affichage_Lieux_tk = Label(EnveloppeInfo_Carbu, text= Affichage_Lieux)    
    Affichage_prix_sp_98_tk = Label(EnveloppeInfo_Carbu, text= Affichage_prix_sp_98)
    Affichage_prix_e10_tk = Label(EnveloppeInfo_Carbu, text= Affichage_prix_e10)
    Affichage_prix_diesel_tk = Label(EnveloppeInfo_Carbu, text= Affichage_prix_diesel)
    Affichage_prix_gpl_tk = Label(EnveloppeInfo_Carbu, text= Affichage_prix_gpl)

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    Affichage_Lieux_tk.pack()
    Affichage_prix_sp_98_tk.pack()
    Affichage_prix_e10_tk.pack()
    Affichage_prix_diesel_tk.pack()
    Affichage_prix_gpl_tk.pack()
    
    #Etape-5 Bouton(s)
    Button(Info_Carbu, text="Fermer", command=Info_Carbu.destroy).pack()  #Bouton de Fermeture de la Fenetre actuelle        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
Button(fenetre, text="Infos GPS", command=Informations_GPS).pack()              #Bouton
Button(fenetre, text="Recherche par Adresse", command=Recherche_Adresse).pack() #Bouton
Button(fenetre, text="Météo Complète", command=Meteo_Complete).pack()           #Bouton 
Button(fenetre, text="Prix du Carburant", command=Prix_du_Carburant).pack()     #Bouton
Button(fenetre, text="Fermer", command=fenetre.destroy).pack()                  #Bouton de Fermeture de la Fenetre Principale        
#-------------------------------------------------------------------Contenue Fenetres Secondaires-------------------------------------------------------------------

if __name__ == "__main__":
    try:
        #-------------------------------------------------------------------Demarrage des fonctions operant sur la Fenetre Principale-------------------------------------------------------------------
        #Récupération des informations pour la Mise à jour du LABEL toute les 1 milliseconde quand la fenêtre Maitre est lancée
        fenetre.after(1, update_temps_actuel)                   #update_temps_actuel()
        fenetre.after(2, update_information_Materiel)           #update_information_Materiel()
        fenetre.after(3, update_information_Complementaire)     #update_information_Complementaire()
        fenetre.mainloop()                                      #Boucle de Lancement de la Fenêtre PRINCIPAL
        #-------------------------------------------------------------------Demarrage des fonctions operant sur la Fenetre Principale---------------------------------------------------------------       
        pass
    
    #---!!!GESTION DES ERREURS!!!---
    #Utiliser uniquement quand le produit est finaliser et/ou commenter les lignes durant le devellopement pour determiner les bugs.
    #except TypeError:
    # print("Code Erreur: TypeError")
    #except KeyError:
    # print("Code Erreur: KeyError")
    #except ValueError:
    # print("Code Erreur: ValueError")
    #except AssertionError:
    # print("Code Erreur: AssertionError")
    #except NameError:
    # print("Il est necessaire de Redemarrez le Programme!")                          #On affiche ce message dans la console
    # print("Code Erreur: NameError")
    except:
     print("Il est necessaire de Redemarrez le Logiciel!")                           #On affiche ce message dans la console
     print("Code Erreur: Aucun")
    #---!!!GESTION DES ERREURS!!!---
