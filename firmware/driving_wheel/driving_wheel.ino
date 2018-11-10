/*
  Reading a serial ASCII-encoded string.

  This sketch demonstrates the Serial parseInt() function.
  It looks for an ASCII string of comma-separated values.
  It parses them into ints, and uses those to fade an RGB LED.

  Circuit: Common-Cathode RGB LED wired like so:
  - red anode: digital pin 3
  - green anode: digital pin 5
  - blue anode: digital pin 6
  - cathode: GND

  created 13 Apr 2012
  by Tom Igoe
  modified 14 Mar 2016
  by Arturo Guadalupi

  This example code is in the public domain.
*/

// pins for the LEDs:
const int left = 9;
const int right = 8;
const int forward = 6;
const int backwards = 7;

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
