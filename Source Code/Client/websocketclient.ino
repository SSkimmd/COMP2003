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

void DisplayCalendar(String data) {
  char* chr = strdup(data.c_str());
  
  Clear();
  Paint_DrawString_EN(10, 20, chr, &Font16, WHITE, BLACK);

  printf("EPD_Display\r\n");
  EPD_7IN5_V2_Display(BlackImage);
  DEV_Delay_ms(2000);  
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
          DisplayCalendar(title);
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
  socketIO.begin("192.168.0.34", 5000, "/socket.io/?EIO=4");

  // event handler
  socketIO.onEvent(socketIOEvent);



  //DISPLAY
  printf("EPD_7IN5_V2_test Demo\r\n");
  DEV_Module_Init();

  printf("e-Paper Init and Clear...\r\n");
  EPD_7IN5_V2_Init();
  EPD_7IN5_V2_Clear();
  DEV_Delay_ms(500);

  UWORD Imagesize = ((EPD_7IN5_V2_WIDTH % 8 == 0) ? (EPD_7IN5_V2_WIDTH / 8 ) : (EPD_7IN5_V2_WIDTH / 8 + 1)) * EPD_7IN5_V2_HEIGHT;
  if ((BlackImage = (UBYTE *)malloc(Imagesize)) == NULL) {
    printf("Failed to apply for black memory...\r\n");
    while (1);
  }
  printf("Paint_NewImage\r\n");
  Paint_NewImage(BlackImage, EPD_7IN5_V2_WIDTH, EPD_7IN5_V2_HEIGHT, 0, WHITE);
  Clear();
}

void Clear() {
  Paint_Clear(WHITE);
}

void displayInfo() {
  printf("SelectImage:BlackImage\r\n");
  Paint_SelectImage(BlackImage);
  Paint_Clear(WHITE);

  // 2.Drawing on the image
  printf("Drawing:BlackImage\r\n");
  Paint_DrawPoint(10, 80, BLACK, DOT_PIXEL_1X1, DOT_STYLE_DFT);
  Paint_DrawPoint(10, 90, BLACK, DOT_PIXEL_2X2, DOT_STYLE_DFT);
  Paint_DrawPoint(10, 100, BLACK, DOT_PIXEL_3X3, DOT_STYLE_DFT);

  Paint_DrawLine(20, 70, 70, 120, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);
  Paint_DrawLine(70, 70, 20, 120, BLACK, DOT_PIXEL_1X1, LINE_STYLE_SOLID);

  Paint_DrawRectangle(20, 70, 70, 120, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
  Paint_DrawRectangle(80, 70, 130, 120, BLACK, DOT_PIXEL_1X1, DRAW_FILL_FULL);
  Paint_DrawCircle(45, 95, 20, BLACK, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
  Paint_DrawCircle(105, 95, 20, WHITE, DOT_PIXEL_1X1, DRAW_FILL_FULL);
  Paint_DrawLine(85, 95, 125, 95, BLACK, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);
  Paint_DrawLine(105, 75, 105, 115, BLACK, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);

  Paint_DrawString_EN(10, 0, "waveshare", &Font16, BLACK, WHITE);
  Paint_DrawString_EN(10, 20, "hello world", &Font12, WHITE, BLACK);

  Paint_DrawNum(10, 33, 123456789, &Font12, BLACK, WHITE);
  Paint_DrawNum(10, 50, 987654321, &Font16, WHITE, BLACK);

  Paint_DrawString_CN(130, 0, "TEST1", &Font12CN, BLACK, WHITE);
  Paint_DrawString_CN(130, 20, "TEST2", &Font24CN, WHITE, BLACK);

  printf("EPD_Display\r\n");
  EPD_7IN5_V2_Display(BlackImage);
  DEV_Delay_ms(2000);
}

void loop() {
    socketIO.loop();
}