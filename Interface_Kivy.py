#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ROCHAT_FRANCK
#Aides: https://kivy.org/doc/stable/guide/lang.html                 #Documenation sur la Synthax a avoir
#Aides: https://kivy.org/doc/stable/api-kivy.uix.label.html         #Documentation sur les differents Widgets de base de Kivy
#Aides: https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html     #Documentation sur le Layout (couche) dit 'BoxLayout' de Kivy
#Aides: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html #Documentation sur les ScreenManagers et leurs fonctionnalités

#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date
#---------------------------------------Importante LIB---------------------------------------

#---------------------------------------Project LIB---------------------------------------
import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

#from pydub import AudioSegment                              #Bibliotheque permettant de jouer des Sons et Jingles
#from pydub.playback import play                             #Bibliotheque permettant de jouer des Sons et Jingles

print("\n Bonjour/Bonsoir, ne pas faire fonctionner ce programme en utilisant les droits/commandes administrateur si l'utilisateur n'est pas l'Admin au quel cas le programme ne fonctionnera pas correctement. \n") #Information a lire dans la console
sys.path.append("/home/"+USERNAME+"/Voitures_Infos/Services")  #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
sys.path.append("/home/"+USERNAME+"/Voitures_Infos/GPS")
#print(USERNAME)                                            #Test debug

from Infos_Hardware import CPU_usage                        #Obtention de l'utilisation du Processeur par le Systeme d'exploitation et ses programmes autour
from Infos_Hardware import CPU_temp                         #Obtention de la Temperature du Processeur sur la carte mere
from Infos_Hardware import SoC_info                         #Obtention des informations concernant le package CPU+GPU
from Infos_Hardware import MEM_info                         #Obtention de l'utilisation de la Memoire Vive du Systeme

from Services_Energies import Energies_Carburants_GPSoI
from Vitesse_Utilisateur import la_Vitesse_GPS
from Meteo import Meteo_Simplifie
from Meteo import main_meteo
from Etat_Signal_GPS import Etat_connection_GPS
from Etat_Lien_WiFi import Affichage_Wifi_UI
from Boussole import Affichage_boussole
#---------------------------------------Project LIB---------------------------------------


#---------------------------------------Kivy LIB---------------------------------------
from kivy.app import App                                        #Utile a Kivy
from kivy.uix.boxlayout import BoxLayout                        #Importation de la disposition BoxLayout
from kivy.uix.anchorlayout import AnchorLayout                  #Importation de la disposition AnchorLayout
from kivy.uix.gridlayout import GridLayout                      #Importation de la disposition GridLayout
from kivy.uix.floatlayout import FloatLayout                    #Importation de la disposition FloatLayout

from kivy.uix.widget import Widget                              #Importation des différents widget disponible
from kivy.properties import StringProperty                      #Importation du StringProperty permettant de faire des variables dynamiques
from kivy.clock import Clock                                    #Importation de Clock permettant de gerer les mises a jour des elements
from kivy.lang import Builder                                   #Importation de Builder pour la lecture et l'interpretation du language KV
from kivy.uix.screenmanager import ScreenManager, Screen        #Importation de ScreenManager/Screen permettant la gestion de plusieurs 'ecran'(aka Fenetre ou page).
from kivy.uix.popup import Popup                                #Importation des Popup de Kivy
from kivy.uix.label import Label                                #Importation des Label de Kivy
from kivy.uix.button import Button                              #Importation des Boutton de Kivy
#---------------------------------------Kivy LIB---------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#Builder.load_string(""" """)           #Saisie indiquant la disposition des elements visuels
Builder.load_file('Interface_Kivy.kv')  #Chargement du fichier qui indique la disposition des elements visuels
#---------------------------------------------------------------------------------------------------------------------------------------
class MaDisposition(BoxLayout, Screen):
    #---Variables a Mettre a jour---

    #--Horloge--
    Time_Horloge = StringProperty()     #Quand cette variable changera, toute les elements comportant cette variable se mettront a jour lorsque sa valeurs changera car elle est specifie 'StringProperty'
    #--Horloge--

    #--Infos Meteo Simplifie--
    meteo_simplifie = StringProperty()
    #--Infos Meteo Simplifie--

    #---Variables a Mettre a jour---

    Voiture_PNG = "/home/"+USERNAME+"/Voitures_Infos/Services/images_defaut/Voiture.png" #Pour indiquer le chemin ou se trouve l'Image dans l'Ordinateur
    
    def __init__(self, **kwargs):
        super(MaDisposition, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        Clock.schedule_interval(self.temps_actuel_update,10)
        
        Clock.schedule_once(self.La_meteo_simplifie)
        Clock.schedule_interval(self.La_meteo_simplifie,3613)
        #---Elements a Mettre a jour---
    
    #---------------------------------------------
    def temps_actuel(self):   
        #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
        #-- DEBUT -- Heure,Minute,Seconde
        tt = time.time()
        system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
        print(("Voici l'heure:",system_time))
        return system_time
        #-- FIN -- Heure,Minute,Seconde
    def temps_actuel_update(self, *args):                                           #On met a jour l'Objet Time_Horloge avec l'heure de la methode precedente
        self.Time_Horloge = MaDisposition.temps_actuel(self)
    #---------------------------------------------

    #---------------------------------------------
    def La_meteo_simplifie(self, *args):
        #Affichage simplifiee de la meteo
        self.meteo_simplifie = Meteo_Simplifie()        
    #---------------------------------------------
    
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
class Infos_Systemes(BoxLayout, Screen):
    print("Classe Infos Systèmes")

    #---Variables a Mettre a jour---
    #--Informations Materiels--
    UtilisationCPU = StringProperty()   
    MemoireUtilise = StringProperty()   
    CPUtemp = StringProperty()
    etat_co_gps = StringProperty()
    etat_co_wifi = StringProperty()
    #--Informations Materiels--
    #---Variables a Mettre a jour---

    def __init__(self, **kwargs):
        super(Infos_Systemes, self).__init__(**kwargs)   #On SuperCharge la classe
        #---Elements a Mettre a jour---
        Clock.schedule_interval(self.information_Materiel,5)                        #On indique a Kivy quand Commencer/Re-commencer l'execution d'une methode
        #---Elements a Mettre a jour---

    #---------------------------------------------
    def information_Materiel(self, *args):
        #Obtention des Informations Materiel de l'Ordinateur      
        self.UtilisationCPU = CPU_usage()                                           #Obtention du Niveau d'utilisation du Processeur.
        self.MemoireUtilise = MEM_info()                                            #Obtention d'information par rapport à la Memoire Vive.
        self.CPUtemp = CPU_temp()                                                   #Obtention de la Temperature du Package Processeur/GPU.
        self.etat_co_gps = Etat_connection_GPS()
        self.etat_co_wifi = Affichage_Wifi_UI()
    #---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
        
#---------------------------------------------------------------------------------------------------------------------------------------
class Infos_GPS(BoxLayout, Screen):
    print("Classe Infos GPS")

    #---Variables a Mettre a jour---
    #--Informations Complementaires--
    boussole_num = StringProperty()
    Vitesse_KMH = StringProperty()
    #--Informations Complementaires--
    #---Variables a Mettre a jour---

    def __init__(self, **kwargs):
        super(Infos_GPS, self).__init__(**kwargs)   #On SuperCharge la classe
        #---Elements a Mettre a jour---
        Clock.schedule_interval(self.information_Complementaire,1)
        #---Elements a Mettre a jour---

    #---------------------------------------------
    def information_Complementaire(self, *args):
        #Recuperation des Informations
        self.Vitesse_KMH = la_Vitesse_GPS()
        self.boussole_num = Affichage_boussole()
    #---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Prix_du_Carburant(BoxLayout, Screen):
    print("Classe pour le Prix du Carburant")
    
    #---Variables a Mettre a jour---        
    #--Infos Energies--
    lieux_carbu = StringProperty()
    prix_sp_98  = StringProperty()
    prix_e10  = StringProperty()
    prix_diesel  = StringProperty()
    prix_gpl  = StringProperty()   
    #--Infos Energies--
    #---Variables a Mettre a jour---

    def __init__(self, **kwargs):
        super(Prix_du_Carburant, self).__init__(**kwargs)   #On SuperCharge la classe

        #---Elements a Mettre a jour---       
        Clock.schedule_once(self.Prix_des_Carbu)
        #---Elements a Mettre a jour---

    #---------------------------------------------
    def Prix_des_Carbu(self, *args):
        #Obtention des prix des differents carburant disponibles pres de l'utilisateur
        #--        
        self.lieux_carbu,self.prix_sp_98,self.prix_e10,self.prix_diesel,self.prix_gpl = Energies_Carburants_GPSoI()
        #--
    #---------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
class LaMeteo(BoxLayout, Screen):
    print("Classe Meteo")

    #---Variables a Mettre a jour---
    
    #--Infos Meteo Complete--
    status_climat = StringProperty()
    climat_min = StringProperty()
    climat_now = StringProperty()
    climat_max = StringProperty()
    vitesse_du_vent = StringProperty()
    volume_de_neige = StringProperty()
    volume_de_pluie = StringProperty()
    pourcentage_humidite = StringProperty()
    couverture_de_nuage = StringProperty()
    #--Infos Meteo Complete--
    
    #---Variables a Mettre a jour---

    #Voiture_PNG = "/home/"+USERNAME+"/Voitures_Infos/Services/images_defaut/Voiture.png" #Pour indiquer le chemin ou se trouve l'Image dans l'Ordinateur
    
    def __init__(self, **kwargs):
        super(LaMeteo, self).__init__(**kwargs)   #On SuperCharge la classe
        #---Elements a Mettre a jour---
        #Exemple:
        #Clock.schedule_once(self.methode)
        #Clock.schedule_interval(self.methode, X Secondes d'interval de rafraichissement)
        Clock.schedule_once(self.La_meteo_complete)
        Clock.schedule_interval(self.La_meteo_complete,3613)
        #---Elements a Mettre a jour---

    #---------------------------------------------
    def La_meteo_complete(self, *args):
        #Recuperation complete de la meteo
        self.status_climat,self.climat_min,self.climat_now,self.climat_max,self.vitesse_du_vent,self.volume_de_neige,self.volume_de_pluie,self.pourcentage_humidite,self.couverture_de_nuage = main_meteo()        
    #---------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Play_Media(AnchorLayout,GridLayout, Screen):
    print("Play_Media")
    #BoucleVideo = "/home/"+USERNAME+"/Voitures_Infos/Services/videos_defaut/bf3_loop.avi" #Pour indiquer le chemin ou se trouve l'Image dans l'Ordinateur
    #Utiliser les fonctions videos avec Kivy sur RPI ou ordinateur lent a pour consequence une leuteur extreme du systeme donc du programme; à eviter si possible.
    #J'aimerais essayer de mettre en place du Multi-processing mais force de constater que ce n'est pas evident a mettre en place.

    #Utiliser les fonctions d'images est plus raisonnnable dans tous les cas de figures mais affiches moins de dynamismes et de vivant au programme Kivy.
    #Par consequent on peut utiliser les fonctions native de kivy pour ajouter du dynamisme au sein du programme avec les transitions par exemple.
    FondImage = "/home/"+USERNAME+"/Voitures_Infos/Services/images_defaut/stars_up.jpg" #Pour indiquer le chemin ou se trouve l'Image dans l'Ordinateur 
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------
class Fonctionnalitee_3(BoxLayout, Screen):
    print("Fonctionnalitee_3")
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------Creation du Screen Manager---------------------------------------------
#HELP: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html
#Dans cette partie du code, on indique les differents 'ecrans' ou fenetres que dispose ce logiciel sous Kivy
sm = ScreenManager()
sm.add_widget(MaDisposition(name ='Accueil'))
sm.add_widget(Infos_Systemes(name='Infos_Systemes'))
sm.add_widget(Infos_GPS(name='Infos_GPS'))
sm.add_widget(Prix_du_Carburant(name='Prix_du_Carburant'))
sm.add_widget(LaMeteo(name='Meteo'))
sm.add_widget(Play_Media(name='Play_Media'))
sm.add_widget(Fonctionnalitee_3(name='Fonctionnalitee_3'))
#---------------------------------------------Creation du Screen Manager---------------------------------------------
      
class Voitures_InfosApp(App):

    def on_start(self):
        #Indique ce que l'on fait au demarage du logiciel.
        pass
    
    def on_stop(self):
        #Indique ce que l'on fait a l'arret du logiciel.
        pass
    
    def build(self):
        #Demarage du Logiciel Kivy.
        return sm
    
if __name__ == "__main__":
    #Demarage du Logiciel Kivy
    Voitures_InfosApp().run()
