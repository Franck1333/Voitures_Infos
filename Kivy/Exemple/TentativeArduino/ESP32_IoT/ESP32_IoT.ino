/*
 * HelTec Automation(TM) ESP32 Series Dev boards OLED
 *
 * - Some OLED draw Simple Function function test;
 *
 * by LXYZN from HelTec AutoMation, ChengDu, China
 * 
 * www.heltec.cn
 *
 * this project also realess in GitHub:
 * https://github.com/HelTecAutomation/Heltec_ESP32
*/
//-------------Blibliotheque du Programme-------------
#include "Arduino.h"
#include "ArduinoJson.h"
#include "heltec.h"
#include "images.h"
#include "font_price.h"
// see http://blog.squix.org/2015/05/esp8266-nodemcu-how-to-create-xbm.html
// on how to create xbm files
//-------------Blibliotheque du Programme-------------

//-------------Configuration_WiFi-------------
#include <WiFi.h>
#include <WiFiMulti.h>
WiFiMulti WiFiMulti;
#include <HTTPClient.h>

#ifndef STASSID
#define STASSID "****"
#define STAPSK  "****"
#endif
const char* ssid     = STASSID;
const char* password = STAPSK;
//-------------Configuration_WiFi-------------

void setup() {
  Serial.begin(115200);
  Heltec.begin(true /*DisplayEnable Enable*/, false /*LoRa Disable*/, true /*Serial Enable*/);
  Heltec.display->flipScreenVertically();
  Heltec.display->setFont(ArialMT_Plain_10);
  // Font Demo1
  // create more fonts at http://oleddisplay.squix.ch/

  Connection_Au_WiFi();
}

void loop() {
  // clear the display
  Heltec.display->clear();
    
  //Hello_World();
  Energie_essence();
   
  // write the buffer to the display
  Heltec.display->display();
}

void Connection_Au_WiFi(){
    delay(10);

    // We start by connecting to a WiFi network
    WiFiMulti.addAP(STASSID, STAPSK);

    Serial.println();
    Serial.println();
    Serial.print("Waiting for WiFi... ");

    while(WiFiMulti.run() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    delay(500);
  }

String Requete_GET(String LIEN){            //Cette fonction permet d'Obtenir des information d'une page Internet par la Methode GET
    Serial.print("Demarrage requete GET...");
    HTTPClient http;                      //Declare an object of class HTTPClient
    http.begin(LIEN);                     //Specify request destination
    int httpCode = http.GET();            //Send the request
    String payload = http.getString();    //Get the request response payload
    Serial.println(payload);              //Print the response payload      
    http.end();                           //Close connection
    delay(2048);                          //Send a request every X seconds
    return payload;
    }

void Hello_World(){
    //Heltec.display->setTextAlignment(TEXT_ALIGN_CENTER);
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(35, 5, "Hello World!");
  }

void Energie_essence(){
    String json = Requete_GET("http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis");

    DynamicJsonDocument doc(1024);
    deserializeJson(doc, json);
    JsonObject obj = doc.as<JsonObject>();
    
    long resultat_json = doc["records"][0]["fields"]["price_sp98"];
    Serial.println(resultat_json);

    char affichage_rslt[64];    
    ltoa(resultat_json,affichage_rslt,10);
    //Serial.println(buff);
    //String affichage_rslt  = "1.559";
    
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(0, 2, "Essence Euro/L");
    
    Heltec.display->setFont(Lato_Black_20);
    Heltec.display->drawString(45,30,affichage_rslt);
  }

void Energie_diesel(){
    String affichage_rslt  = "1.449";
  
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(0, 2, "Diesel Euro/L");
    
    Heltec.display->setFont(Lato_Black_20);
    Heltec.display->drawString(45,30,affichage_rslt);
  }

void Energie_fioul(){
    String affichage_rslt  = "0.917";
  
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(0, 2, "Fioul Euro/L");
    
    Heltec.display->setFont(Lato_Black_20);
    Heltec.display->drawString(45,30,affichage_rslt);
  }


void Energie_electricite(){
    String affichage_rslt  = "0.1467";
  
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(0, 2, "Electricite Euro/kWh");
    
    Heltec.display->setFont(Lato_Black_20);
    Heltec.display->drawString(45,30,affichage_rslt);
  }

void Energie_eau(){
    String affichage_rslt  = "3.98";
  
    Heltec.display->setFont(ArialMT_Plain_10);
    Heltec.display->drawString(0, 2, "Eau Euro/m3");
    
    Heltec.display->setFont(Lato_Black_20);
    Heltec.display->drawString(45,30,affichage_rslt);
  }
