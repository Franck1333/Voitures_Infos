//AIDE: https://openclassrooms.com/fr/courses/1056721-des-applications-ultra-rapides-avec-node-js/1057503-le-framework-express-js

var express = require('express'); //npm install express //npm install ejs

var app = express();

app.use(express.static(__dirname + '/public')); //Pour le partage des fichiers CSS.

app.get('/', function(req, res) {
  var system_time = "12h13";
  res.render('index.ejs', {system_time: system_time});
});

app.get('/Infos_Systeme', function(req, res) {
  var UtilisationCPU = "13%";
  var MemoireUtilise = "3%";
  var tk_cputemp = "temp=60°C";
  var Affichage_etat_gps = "GPS = OK";
  var Etat_Wifi_UI = "WiFi Connecter";
  res.render('Infos_Systeme.ejs', {UtilisationCPU: UtilisationCPU, MemoireUtilise: MemoireUtilise, tk_cputemp: tk_cputemp, Affichage_etat_gps: Affichage_etat_gps, Etat_Wifi_UI: Etat_Wifi_UI });
});

app.get('/Infos_GPS', function(req, res) {
  var tk_tel_urgence = "Appel d'urgence de votre continent : 112";
  var packed_boussole = "***Coordonnées GPS ici***"
  var Affichage_KMH = "73 Km/h"
  res.render('Infos_GPS.ejs', {tk_tel_urgence: tk_tel_urgence, packed_boussole: packed_boussole, Affichage_KMH: Affichage_KMH});
});

app.get('/Meteo_Complete', function(req, res) {
  var tk_climat_min = "Temp min : 13°C"
  var tk_climat_max = "Temp max : 26°C"
  var tk_climat_now = "Temp actuel : 23°C"
  var tk_vitesse_du_vent = "Vitesse du Vent: 16 m/s"
  var tk_status_climat = "En bref: Eclairci"
  var tk_volume_de_neige = "0 L"
  var tk_volume_de_pluie = "0 L"
  var tk_couverture_de_nuage = "19%"
  var tk_pourcentage_humidite = "35%"
  res.render('Meteo_Complete.ejs', {tk_climat_min: tk_climat_min,tk_climat_max: tk_climat_max,tk_climat_now: tk_climat_now, tk_vitesse_du_vent:tk_vitesse_du_vent, tk_status_climat:tk_status_climat, tk_volume_de_neige:tk_volume_de_neige, tk_volume_de_pluie:tk_volume_de_pluie, tk_couverture_de_nuage:tk_couverture_de_nuage, tk_pourcentage_humidite:tk_pourcentage_humidite });
});

app.get('/Prix_du_Carburant', function(req, res) {
  var Affichage_Lieux = "Chemille/Mer"
  var Affichage_prix_sp_98 = "1.25 €/L"
  var Affichage_prix_e10 = "1.22 €/L"
  var Affichage_prix_diesel = "1.12 €/L"
  var Affichage_prix_gpl = "0.882 €/L"
  res.render('Prix_du_Carburant.ejs', {Affichage_Lieux: Affichage_Lieux, Affichage_prix_sp_98:Affichage_prix_sp_98, Affichage_prix_e10:Affichage_prix_e10,Affichage_prix_diesel:Affichage_prix_diesel,Affichage_prix_gpl:Affichage_prix_gpl});
});

/*app.get('/compter/:nombre', function(req, res) {
  var noms = ['Robert', 'Jacques', 'David'];
  res.render('page.ejs', {compteur: req.params.nombre, noms: noms});
});*/

app.listen(8080);