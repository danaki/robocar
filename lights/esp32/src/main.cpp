#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include "FS.h"
#include <LITTLEFS.h>

// Replace with your network credentials
const char* ssid = "robo";
const char* password = "robotraffic";

typedef struct {
  byte r;
  byte y;
  byte g;
  unsigned int time;
} State;

struct {
  byte r;
  byte y;
  byte g;
} pins = {5, 4, 2};

State states[] = {
  {1, 0, 0, 5000},
  {1, 1, 0, 2000},
  {0, 0, 1, 5000},
  {0, 0, 0, 500},
  {0, 0, 1, 500},
  {0, 0, 0, 500},
  {0, 0, 1, 500},
  {0, 0, 0, 500},
  {0, 0, 1, 500},
  {0, 3, 0, 2000},
};

unsigned int currentState;
boolean isPaused;

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);
AsyncEventSource events("/events");

String processor(const String& var)
{
  if (var == "IP") {
    return WiFi.localIP().toString();
  }

  return String();
}

int colorToPin(char color)
{
  switch (color) {
    case 'r': return pins.r;
    case 'y': return pins.y;
    case 'g': return pins.g;
  }

  return 0;
}

void reset()
{
  digitalWrite(pins.r, 0);
  digitalWrite(pins.y, 0);
  digitalWrite(pins.g, 0);
}

void notFound(AsyncWebServerRequest *request)
{
  request->send(404, "text/plain", "Nothing here..");
}

void sendPinState()
{
  char buf[10];
  sprintf(buf, "%d %d %d", digitalRead(pins.r), digitalRead(pins.y), digitalRead(pins.g));
  events.send(buf, "pin", millis());
}

void setup()
{
  currentState = 0;
  isPaused = false;

  Serial.begin(115200);

  if (! LittleFS.begin()) {
    Serial.println("LITTLEFS Mount Failed");
    return;
  }

  pinMode(pins.r, OUTPUT);
  pinMode(pins.y, OUTPUT);
  pinMode(pins.g, OUTPUT);

  reset();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
    digitalWrite(pins.r, ! digitalRead(pins.r));
    digitalWrite(pins.y, ! digitalRead(pins.y));
    digitalWrite(pins.g, ! digitalRead(pins.g));
  }

  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->send(LittleFS, "/index.html", String(), false, processor);
  });

  server.on("/update", HTTP_GET, [] (AsyncWebServerRequest *request) {
    char color = request->hasParam("color") ? request->getParam("color")->value().charAt(0) : '_';
    int value = request->hasParam("value") ? request->getParam("value")->value().toInt() : 0;

    int pin = colorToPin(color);
    if (color && pin) {
      digitalWrite(pin, value);
      request->send(200, "text/plain", "OK");
    } else {
      request->send(400, "text/plain", "");
    }
  });

  server.on("/pause", HTTP_POST, [](AsyncWebServerRequest *request) {
    Serial.println("Paused");
    isPaused = true;
    request->send(200, "text/plain", "OK");
  });

  server.on("/start", HTTP_POST, [](AsyncWebServerRequest *request) {
    Serial.println("Starting");
    isPaused = false;
    currentState = 0;
    reset();
    request->send(200, "text/plain", "OK");
  });

  // server.on("/refresh", HTTP_POST, [](AsyncWebServerRequest *request) {
  //   request->send(200, "text/plain", "OK");
  // });

  server.serveStatic("/", LittleFS, "/");

  server.onNotFound(notFound);
  server.addHandler(&events);
  server.begin();
}

void loop()
{
  if (isPaused) {
    delay(1000);
    sendPinState();
  } else {
    Serial.printf("state = %d %d %d %d %d\n", currentState, states[currentState].r, states[currentState].y, states[currentState].g, states[currentState].time);

    digitalWrite(pins.r, states[currentState].r);
    digitalWrite(pins.y, states[currentState].y);
    digitalWrite(pins.g, states[currentState].g);

    sendPinState();

    delay(states[currentState].time);

    currentState++;

    if (currentState >= (sizeof(states) / sizeof(State))) {
      currentState = 0;
    }
  }
}