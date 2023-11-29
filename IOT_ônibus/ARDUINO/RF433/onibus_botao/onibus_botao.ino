#include <RH_ASK.h>
#include <SPI.h>
//Padrão porta 12
RH_ASK rf_driver;

const int A = 8;
const int B = 7;
const int C = 6;
const int D = 5;
const int E = 4;
const int F = 3;

void setup() {
  pinMode(A, INPUT);
  pinMode(B, INPUT);
  pinMode(C, INPUT);
  pinMode(D, INPUT);
  pinMode(E, INPUT);
  pinMode(F, INPUT);
  rf_driver.init();
  Serial.begin(9600);
}

void loop() {
  int value8 = digitalRead(A);
  int value7 = digitalRead(B);
  int value6 = digitalRead(C);
  int value5 = digitalRead(D);
  int value4 = digitalRead(E);
  int value3 = digitalRead(F);
  if (value8 == HIGH) {
    const char *msg = "a_165_2001_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
  if (value7 == HIGH) { 
    const char *msg = "b_165_2001_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
  if (value6 == HIGH) {
    const char *msg = "c_165_2001_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
  if (value5 == HIGH) {
    const char *msg = "a_209_2002_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
  if (value4 == HIGH) {
    const char *msg = "b_209_2002_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
  if (value3 == HIGH) {
    const char *msg = "c_209_2002_0"; 
    rf_driver.send((uint8_t *)msg, strlen(msg));
    delay(1000);
  }
}
