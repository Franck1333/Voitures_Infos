//WORK "GPS": https://gist.github.com/Franck1333/440ed64edd6b3c941c3947eb071fdc19
//WORK "OLED": https://gist.github.com/Franck1333/133faba76fa7695bb177bbba9376cf86

//---Screen Lib---
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
//---Screen Lib---

//---GPS Lib---
#include <SoftwareSerial.h>
#include <TinyGPS++.h>
//---GPS Lib---

//---Screen Definition---
#define SCREEN_WIDTH 128 //OLED display width, in pixels
#define SCREEN_HEIGHT 32 //OLED display height, in pixels
//Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET  4 //Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
//---Screen Definition---

//---GPS Definition---
// Choose two Arduino pins to use for software serial
int RXPin = 2;
int TXPin = 3;
//Default baud of NEO-6M is 9600
int GPSBaud = 9600;
// Create a TinyGPS++ object
TinyGPSPlus gps;
// Create a software serial port called "gpsSerial"
SoftwareSerial gpsSerial(RXPin, TXPin);
//---GPS Definition---

void setup() {
  Serial.begin(9600);

  //---INIT_SCREEN---
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }
  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  // Clear the buffer
  display.clearDisplay();
  delay(2048);
  //---INIT_SCREEN---

  //---INIT_GPS---
  // Start the software serial port at the GPS's default baud
  gpsSerial.begin(GPSBaud);
  //---INIT_GPS---

  //HelloWorld();
}

void loop() {
  // put your main code here, to run repeatedly:
Infos_GPS();
}



float Coord_GPS(void){
  float latitude = gps.location.lat();          //Latitude en degres
  float longitude = gps.location.lng();         //Longitude en degres
    
  Serial.println("^  _  ^");                    //Cette ligne permet de délimiter les nouvelles infos par rapport aux anciennes dans la console 
  Serial.print("Latitude: ");
  Serial.println(latitude ,6);                  //Cette ligne permet d'afficher la Latitude de l'utilisateur en affichant uniquement les six premières valeurs
  Serial.print("Longitude: ");
  Serial.println(longitude ,6);                 //Cette ligne permet elle aussi d'afficher la Longitude de l'utilisateur avec uniquement les 6 premières valeurs

  //Je n'ai pas effectue le traitement d'afichage de ces données car je ne reçois pas de signal correcte pour experimenter pour le moment.

  delay(2048);
  }


float Infos_GPS(void){
  uint32_t dateGPS = gps.date.value();        //Obtention de la date via GPS (uint32_t)
  float vitesse_utilisateur = gps.speed.kmph(); //Obtention de la Vitesse de mouvement en Kilometre par Heure de l'utilisateur
  uint32_t captation = gps.satellites.value();  //Inidcation du nombre de Satellite capté au meme moment

  Serial.print("La Date: ");
  Serial.println(dateGPS);
  Serial.print("Votre Vitesse: ");
  Serial.println(vitesse_utilisateur);
  Serial.print("Qt Satellite Capté: ");
  Serial.println(captation);

  display.setTextColor(WHITE);          //La couleur du texte
  display.setCursor(0,0);               //On va ecrire en x=0, y=0
  display.print("La date: ");              //Un println pour écrire du texte sur l'ecran
  display.println(dateGPS);

  display.setTextColor(WHITE);          //La couleur du texte
  display.setCursor(0,10);              //On va ecrire en x=0, y=10
  display.print("Votre Vitesse: ");           //Un println pour écrire du texte sur l'ecran
  display.println(vitesse_utilisateur);

  display.setTextColor(WHITE);          //La couleur du texte
  display.setCursor(0,20);              //On va ecrire en x=0, y=20
  display.print("Satellites captes:");        //Un println pour écrire du texte sur l'ecran
  display.println(captation);
  
  display.display();                    //Affichage du Resultat
  delay(512);
  }



/*void HelloWorld(void){
  Serial.println("HelloWorld!!!");  //Message visible dans la console
  
  display.setTextColor(WHITE);      // La couleur du texte
  display.setCursor(0,0);           // On va ecrire en x=0, y=0
  display.print("Hello,");          // Un println pour écrire du texte sur l'ecran
  display.println(" world!");
  display.display();                // Affichage du Resultat
  }*/
