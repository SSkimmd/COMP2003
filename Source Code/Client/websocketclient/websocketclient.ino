#include <DEV_Config.h>
#include <EPD.h>
#include <GUI_Paint.h>
#include <fonts.h>

/*
 * WebSocketClientSocketIOack.ino
 *
 *  Created on: 20.07.2019
 *
 */

#include <Arduino.h>

#include <WiFi.h>
#include <WiFiMulti.h>
#include <WiFiClientSecure.h>

#include <WebSocketsClient.h>
#include <SocketIOclient.h>
#include <ArduinoJson.h>

WiFiMulti WiFiMulti;
SocketIOclient socketIO;
UBYTE *BlackImage;

#define USE_SERIAL Serial


void SendJson(String event, String message) {
  DynamicJsonDocument doc(1024);
  JsonArray array = doc.to<JsonArray>();
  array.add(event);

  JsonObject param1 = array.createNestedObject();
  param1["message"] = message;

  String output;
  serializeJson(doc, output);
  socketIO.sendEVENT(output);
}

void SendLogin(String username, String password) {
  DynamicJsonDocument doc(1024);
  JsonArray array = doc.to<JsonArray>();
  array.add("login");

  JsonObject param1 = array.createNestedObject();
  param1["username"] = username;

  JsonObject param2 = array.createNestedObject();
  param2["password"] = password;

  String output;
  serializeJson(doc, output);
  socketIO.sendEVENT(output);
}

DynamicJsonDocument GetJson(uint8_t * payload, size_t length) {
  char * sptr = NULL;
  int id = strtol((char *)payload, &sptr, 10);
  if(id) {
      payload = (uint8_t *)sptr;
  }
  DynamicJsonDocument doc(1024);
  DeserializationError error = deserializeJson(doc, payload, length);
  return doc;
}

void DisplayCalendar(DynamicJsonDocument data) {
  Clear();
  JsonArray items = data[1]["calendar"].as<JsonArray>();

  int i = 0;
  for(JsonVariant v : items) {
    String str = v["name"].as<String>();
    const char* chr = str.c_str();
    Paint_DrawString_EN(10, i, chr, &Font20, WHITE, BLACK); 
    i += 30;
  }

  EPD_7IN5_V2_Display(BlackImage);
}


void socketIOEvent(socketIOmessageType_t type, uint8_t * payload, size_t length) {
    switch(type) {
        case sIOtype_DISCONNECT:
          break;
        case sIOtype_CONNECT: {
          socketIO.send(sIOtype_CONNECT, "/");
          SendLogin("testusername", "testpassword");
        }
          break;
        case sIOtype_EVENT: {
          DynamicJsonDocument data = GetJson(payload, length);

          String title = data[0];
          SendJson("text", title);

          DisplayCalendar(data);
        }
          break;
        case sIOtype_ERROR:
          break;
    }
}

void setup() {
  WiFiMulti.addAP("", "");

    //WiFi.disconnect();
  while(WiFiMulti.run() != WL_CONNECTED) {
    delay(100);
  }

  String ip = WiFi.localIP().toString();

  // server address, port and URL
  socketIO.begin("192.168.0.19", 5000, "/socket.io/?EIO=4");

  // event handler
  socketIO.onEvent(socketIOEvent);

  DEV_Module_Init();
  EPD_7IN5_V2_Init();

  UWORD Imagesize = ((EPD_7IN5_V2_WIDTH % 8 == 0) ? (EPD_7IN5_V2_WIDTH / 8 ) : (EPD_7IN5_V2_WIDTH / 8 + 1)) * EPD_7IN5_V2_HEIGHT;
  if ((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) {
    printf("Failed to apply for black memory...\r\n");
    while (1);
  }
  Paint_NewImage(BlackImage, EPD_7IN5_V2_WIDTH, EPD_7IN5_V2_HEIGHT, 0, WHITE);
  Clear();
}

void Clear() {
  Paint_Clear(WHITE);
}

void loop() {
  socketIO.loop();
}