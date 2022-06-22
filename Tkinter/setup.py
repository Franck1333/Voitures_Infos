#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides : The generator "set-me-up.py" need a "__init__.py" file in the main root directorie to work .
#HOW INSTALL AND USE THIS PROJECT:
#in the console : sudo python setup.py install
#And all the depencies will be installed with the Project
#Listing env> sudo pip freeze > list.txt

#git clone https://github.com/Franck1333/Voitures_Infos.git

from setuptools import setup, find_packages

setup(
    name='Voitures_Infos',
    version="1.13",
    author='Franck Rochat',
    author_email='rochat.franck@gmail.com',
    description='This software got you some interesting infos when you go somewhere.',
    url='https://github.com/Franck1333/Voitures_Infos',
    license='lgpl',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyserial==3.2.1","geopy==1.20.0","matplotlib==3.0.3","numpy==1.22.0","pandas==0.25.1","pynmea2==1.15.0","pyowm==2.9.0","requests==2.22.0","Unidecode==1.1.1","urllib3==1.26.5","wifi==0.3.8"], #Get the Dependencies from Pypi (pip install)
    dependency_links=[], #Get the Dependencies via HTTP(s)
)
