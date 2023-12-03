#include <RH_ASK.h>
#include <SPI.h>

RH_ASK rf_driver;

const int D = 9;
const int C = 8;
const int B = 7;

void setup() {
  pinMode(C, INPUT);
  pinMode(B, INPUT);
  pinMode(D, INPUT);
  rf_driver.init();
  Serial.begin(9600);
}

char *msg = "bc_165_2001_0";

void loop() {  
  int value8 = digitalRead(C);
  int value7 = digitalRead(B);
  int value9 = digitalRead(D);

  if (value8 == HIGH) {
    msg[0] = 'c';
    msg[1] = 'b';
  }
  if (value7 == HIGH) { 
    msg[0] = 'b';
    msg[1] = 'c';
  }
  if (value9 == HIGH) { 
    msg[0] = 'x';
    msg[1] = 'y';
  }

  rf_driver.send((uint8_t *)msg, strlen(msg));
  delay(1000);
}

