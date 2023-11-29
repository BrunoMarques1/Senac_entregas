#include <SoftwareSerial.h>

SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  meuSerial.begin(9600);
}

void loop() {
  const char *msgSerial = "cb_165_2000_0";
  meuSerial.println(msgSerial);
  delay(500);
}
