#include <Arduino.h>

/*
Project X - Controller (using ESP8266 and stock RC controller)

Connects to a PC to send movement orders to the RC car
*/

// pins for the LEDs:
const int left = 16;
const int right = 4;
const int forward = 0;
const int backwards = 2;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);
  pinMode(forward, OUTPUT);
  pinMode(backwards, OUTPUT);

}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {

    // look for the next valid integer in the incoming serial stream:
    char command = Serial.read();

    switch(command)
    {
      case 'a':
        digitalWrite(left, HIGH);
        delay(100);
        digitalWrite(left, LOW);
        break;

      case 'd':
        digitalWrite(right, HIGH);
        delay(100);
        digitalWrite(right, LOW);
        break;

      case 'w':
        digitalWrite(forward, HIGH);
        delay(100);
        digitalWrite(forward, LOW);
        break;

      case 's':
        digitalWrite(backwards, HIGH);
        delay(100);
        digitalWrite(backwards, LOW);
        break;


     case 't':
        digitalWrite(left, HIGH);
        break;

      case 'y':
        digitalWrite(right, HIGH);
        break;

      case 'u':
        digitalWrite(forward, HIGH);
        break;

      case 'i':
        digitalWrite(backwards, HIGH);
        break;


      case 'g':
        digitalWrite(left, LOW);
        break;

      case 'h':
        digitalWrite(right, LOW);
        break;

      case 'j':
        digitalWrite(forward, LOW);
        break;

      case 'k':
        digitalWrite(backwards, LOW);
        break;

      default:
        break;
    }
  }
}
