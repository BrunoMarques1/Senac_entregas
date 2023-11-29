#include <SoftwareSerial.h>
SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  meuSerial.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (meuSerial.available() > 0) {
    String mensagemSerial = meuSerial.readStringUntil('\n');
    Serial.println(mensagemSerial);
  }
}
