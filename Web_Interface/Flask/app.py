#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/
#https://stackoverflow.com/questions/35116579/how-to-make-page-content-dynamic-with-flask

#ROCHAT_FRANCK
#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from flask import Flask, render_template                    #Lib Flask
#---------------------------------------Importante LIB---------------------------------------

app = Flask(__name__)
@app.route('/')
def index():
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print(("Voici l'heure:",system_time))
    
    return render_template('index.html', system_time=system_time)

@app.route('/Infos_Systeme')
def Informations_Systeme():
    return render_template('Infos_Systeme.html')

@app.route('/Infos_GPS')
def Informations_GPS():
    return render_template('Infos_GPS.html')

@app.route('/Meteo_Complete')
def Meteo():
    return render_template('Meteo_Complete.html')

@app.route('/Prix_du_Carburant')
def PrixCarburant():
    return render_template('Prix_du_Carburant.html')

#LANCEMENT
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
