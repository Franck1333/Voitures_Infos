*This project is a pretext for me to get more knowledge about UIs and packaging programs*

*The doc is not up to date, please wait...*

<h1 id="voitures_infos">Voitures_Infos</h1>
<p>This software got you some interesting infos when you go somwhere.</p>
<p><a href="https://i.ibb.co/8DNC51m/Annotation-2020-03-28-204223.png"><img src="https://i.ibb.co/8DNC51m/Annotation-2020-03-28-204223.png" alt="Image"></a></p>
<h2 id="getting-started">Getting Started</h2>
<p>To get a copy of the project, you can go on the GitHub’s webpage of the project and click on the green button to download as a .ZIP file. However, if you’re using a prompt console on an Unix machine use this line :</p>
<pre><code>git clone https://github.com/Franck1333/Voitures_Infos.git
</code></pre>
<h3 id="prerequisites">Prerequisites</h3>
<p>To use the project, you will need some Hardware :</p>
<pre><code>A Raspberry Pi (Last Version is better) or any Linux computer compatible,
An Internet Connection,
A Micro S.D card (8 Gb Minimum),
An USB G.P.S (Ublox-7) --&gt;  http://amzn.eu/aG9vR3t,
A Display.
</code></pre>
<p>And you will also need some libraries and softwares :</p>
<pre><code>- Python version 3
- Kivy up to date
- An OS up to date
</code></pre>
<p>Be sure to be Up to date with your OS and Python3 environement with this command line:</p>
<pre><code>- sudo apt-get update &amp;&amp; sudo apt-get upgrade &amp;&amp; sudo pip3 install --upgrade pip
</code></pre>

### This commmand line must be executed anyway to install the Virtual Keyboard  *Florence* : 
#### The  *Florence's* Software :
```
  sudo apt-get install florence && sudo apt-get install at-spi2-core
```

<h3 id="downloadinginstalling">Downloading/Installing</h3>
<p>To get and downloaded the files, use this line :</p>
<pre><code>git clone https://github.com/Franck1333/Voitures_Infos.git
</code></pre>
<p>When the project is Downloaded, check your <code>pi</code> folder, and you will see the folder <code>Voitures_Infos</code> .</p>
<p>When you did it, you will have to launch the file called <code>setup.py</code> to install the dependencies neccessary for the project with this command line :</p>
<pre><code>  sudo python3 setup.py install
</code></pre>
<p>There is another way to install all the dependencies needed:</p>
<pre><code>sudo pip3 install -r requirements.txt
</code></pre>
<p>If some problem during the installation occured, please execute this command :</p>
<pre><code>  sudo pip3 install pandas numpy matplotlib kivy geopy pynmea2 pyowm requests Unidecode urllib3 wifi pyserial
</code></pre>
<h2 id="run">Run</h2>
<h4 id="the-way-to-run-the-project-">The Way to run the project :</h4>
<p>To run the project; if you want to see the console activities, you can launch the file called <code>Interface_Kivy.py</code>  into the Command Line Prompt with <code>python3 Interface_Kivy.py</code> in the main folder.</p>
<p>Please don’t use <code>sudo</code>, it’s will not work as expected.</p>
<h2 id="running-the-tests">Running the tests</h2>
<p>That’s how to test features:</p>
<pre><code>python3 &lt;file&gt;.py
</code></pre>
<h2 id="the-folders-and-files">The Folders and Files</h2>
<p>In this project we’ve got some folders</p>
<h4 id="folders">Folders</h4>
<pre><code>Example : 	Any help or example that I used for the project
Services:	Main features
GPS : 		Features which use the GPS
</code></pre>
<h4 id="files-in-voitures_infosservices">Files in “/Voitures_Infos/Services/”</h4>
<p>Main features of the program</p>
<pre><code>- Info_Hardware.py: This feature allow to the Main program to get informations about the status of processors(Usage,Temp),RAM(Usage).
- Etat_Lien_WiFi.py: This program allow to get infos about the Wi-Fi link in real time (like quality of the signal out 70).
- Services_Energies.py : This service allow to the user to get informations about the price of different kind of fuel of where it's located. 
- Vitesse_Utilisateur.py: This service gives to the user his speed (Kilometers per Hours Km/h).
- Consommation_Carburant.py: This service makes some arithmetic about the consumption of fuel; this service will be integrated in the whole program when it's will be ready.
</code></pre>
<p>Folders inside</p>
<pre><code>- Sounds: Sound Pack used by the Main Program. 
- images_defaut &amp; videos_defaut: Images and Videos used by the Main Program. 
</code></pre>
<h4 id="files-in-voitures_infosgps">Files in “/Voitures_Infos/GPS/”</h4>
<p>GPS features of the program</p>
<pre><code>- Etat_Signal_GPS.py: This Servis gives the Status about the GPS link in real time.
- Boussole.py : Get Compass data by using the "Recuperation_Determination.py" file's data.
- GPSoI.py : Get the location of the user's IP Adress.
- Meteo.py : Get the Weather's data by using *pyown API* and the "Recuperation_Determination.py" file's data.
- Recuperation_DeterminationV2.py : Get information come from the GPS USB stick and determinate the location.
- ISS_locate.py : Get data about the ISS location in real time and the forecast of the next visible passage of the I.S.S in the sky above your head.
- Map_YANDEX.py : Get a map in the JPG format about your location and the ISS location in real time.
- emergency_number.py : Get the emergencies Numbers from where your IP adress is located in the world.
- Recuperation_FR_GPS.py : This service is used to test the USB GPS STICK if we've got a Signal or not.
- nettoyage_du_cache.py : This useful feature allows you to clean up your folder of the Python cache files.
</code></pre>
<p>Folders inside</p>
<pre><code>- MAP_downloads: Maps which got downloaded by the use of YANDEX services. 
- Original: I kept the ancient files to renovate all the old stuff and update it. 
</code></pre>
<h2 id="authors">Authors</h2>
<ul>
<li><strong>Franck ROCHAT</strong>  -  <em>Initial work</em>  -  <a href="https://github.com/Franck1333">Franck ROCHAT</a>  Thank You !  ❤️</li>
</ul>
<p><a href="https://goopics.net/i/51JA2"><img src="https://i.goopics.net/51JA2.jpg" alt="Image"></a></p>

