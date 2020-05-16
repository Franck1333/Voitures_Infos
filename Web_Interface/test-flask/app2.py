#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#ROCHAT_FRANCK
#https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/
#https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent/
#---------------------------------------Importante LIB---------------------------------------
import os                                                   #Blibliotheque permettant l'interaction avec le systeme
import sys                                                  #Blibliotheque permettant l'interaction avec le systeme
import datetime                                             #Blibliotheque permettant d'obtenir la date
import time                                                 #Blibliotheque permettant d'obtenir la date

import getpass                                              #On importe la blibliotheque "getpass"
global USERNAME
USERNAME = getpass.getuser()                                #On enregistre le Nom de l'Utilisateur

from flask import Flask, render_template                    #Lib Flask
from flask_socketio import SocketIO, emit
#from threading import Thread, Event
import threading
#---------------------------------------Importante LIB---------------------------------------
app = Flask(__name__)
socketio = SocketIO(app)

def horloge_flask():
   #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
   #-- DEBUT -- Heure,Minute,Seconde
   tt = time.time()
   system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
   print(("Voici l'heure:",system_time))
   emit('my_horloge',system_time)
   #time.sleep(5)

@app.route('/')
def index():
   return render_template('index.html')

@socketio.on('connect')
def connection_client():
      print('Client connecté')
      global threadHorloge
      threadHorloge = threading.Thread(target=horloge_flask)

      #Start the thread only if the thread has not been started before.
      if not threadHorloge.is_alive():
         print("Demarrage du Thread")
         #threadHorloge = socketio.start_background_task(horloge_flask)
         threadHorloge.start()
   #>>RuntimeError: Working outside of request context.


#LANCEMENT
if __name__ == '__main__':
    socketio.run(app,debug=True, host='0.0.0.0')
