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
sys.path.append("/home/"+USERNAME+"/CryptoWatch-Tkinter/Services")  #On indique au systeme ou ce situe le repertoire "Services" dans l'Appareil
#print(USERNAME)                                            #Test debug

#from nettoyage_du_cache import clear_cache                 #Bibliotheque permettant de nettoyer les fichiers cache PYTHON

from Infos_Hardware import CPU_usage                        #Obtention de l'utilisation du Processeur par le Systeme d'exploitation et ses programmes autour
from Infos_Hardware import CPU_temp                         #Obtention de la Temperature du Processeur sur la carte mere
from Infos_Hardware import SoC_info                         #Obtention des informations concernant le package CPU+GPU
from Infos_Hardware import MEM_info                         #Obtention de l'utilisation de la Memoire Vive du Systeme
#-----------------------------------------------------Localisation de l'emplacement des fichiers necessaires-----------------------------------------------------

#-------------Fenetre Maitre-------------
fenetre = Tk()              #Creation d'une Fenetre Maîtresse TK appeler "fenetre"
#-------------Fenetre Maitre-------------

#-------------------------------------------------------------------Contenue Fenetre Principale-------------------------------------------------------------------
#------------------------------------------------------------------------------     #Affichage du Temps HEURES/MINUTES/SECONDES
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
    EnveloppeInfoMateriel.pack(fill="both", expand="no")                                                       #Position de la "Zone Frame" à Label dans la fenêtre
    tk_UtilisationCPU = Label(EnveloppeInfoMateriel, text=UtilisationCPU)
    tk_MemoireUtilise = Label(EnveloppeInfoMateriel, text=MemoireUtilise)
    tk_tk_cputemp = Label(EnveloppeInfoMateriel, text=tk_cputemp)
    tk_UtilisationCPU.pack()
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
    global tk_info_supp
    #Recuperation des Informations  
    INFOS_SUPP = "Aucune Informations Supp. à affichée pour le moment."

    #--Affichage--
    EnveloppeInfoComplementaire = LabelFrame(fenetre, text="Informations Complémentaires", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeInfoComplementaire.pack(fill="both", expand="no")

    #---Affichage Infos---
    tk_info_supp = Label(EnveloppeInfoComplementaire, text= INFOS_SUPP)
    tk_info_supp.pack()
    #---Affichage Infos---    
    #--Affichage--
    
def update_information_Complementaire():
    #Mise à Jour des Informations reçues
    tk_info_supp["text"] = INFOS_SUPP
    
    # Après 2,16 minutes , on met à jour le contenue text du LABEL
    fenetre.after(130000, update_information_Complementaire)
#---
information_Complementaire() #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Fonctionnalitee_1():    
    print("Fonctionnalitée 1")
    
    #Etape-1 On Declare la fenetre
    global Fonct_1
    Fonct_1 = Toplevel()

    #Etape-2 On recupere les informations a afficher
    Informations = "Voici la fonctionnalite Numero #1"

    #Etape-3 On fait la mise en page des Informations receptionner
    #Zone d'affichage
    EnveloppeFonction1 = LabelFrame(Fonct_1, text="Emplacement dédié a l'information", padx=5, pady=5)    #Création d'une "Zone Frame" à Label
    EnveloppeFonction1.pack(fill="both", expand="no")                                                     #Position de la "Zone Frame" à Label dans la fenêtre

    Chocolat = Label(EnveloppeFonction1, text="Chocolat")    
    Noisette = Label(EnveloppeFonction1, text="Noisette")
    Lait = Label(EnveloppeFonction1, text="Lait")
    Vitamine = Label(EnveloppeFonction1, text="Vitamine")

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    Chocolat.pack()
    Noisette.pack()
    Lait.pack()
    Vitamine.pack()
    
    #Etape-5 Bouton(s)
    Button(Fonct_1, text="Fermer", command=Fonct_1.destroy).pack()  #Bouton de Fermeture de la Fenetre actuelle        
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Fonctionnalitee_2():
    print("Fonctionnalitée 2")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Fonctionnalitee_3():
    print("Fonctionnalitée 3")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
Button(fenetre, text="Fonctionnalitée 1", command=Fonctionnalitee_1).pack() #Bouton
Button(fenetre, text="Fonctionnalitée 2", command=Fonctionnalitee_2).pack() #Bouton 
Button(fenetre, text="Fonctionnalitée 3", command=Fonctionnalitee_3).pack() #Bouton
Button(fenetre, text="Fermer", command=fenetre.destroy).pack()              #Bouton de Fermeture de la Fenetre Principale        
#-------------------------------------------------------------------Contenue Fenetres Secondaires-------------------------------------------------------------------

if __name__ == "__main__":
    try:
        #clear_cache()
        #-------------------------------------------------------------------Demarrage des fonctions operant sur la Fenetre Principale-------------------------------------------------------------------
        #Récupération des informations pour la Mise à jour du LABEL toute les 1 milliseconde quand la fenêtre Maitre est lancée
        fenetre.after(1, update_temps_actuel)                #update_temps_actuel()
        fenetre.after(1, update_information_Materiel)        #update_information_Materiel()
        #fenetre.after(1, update_information_Complementaire) #update_information_Complementaire()
        fenetre.mainloop()                                   #Boucle de Lancement de la Fenêtre PRINCIPAL
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
