#include <SoftwareSerial.h>
#include <RH_ASK.h>

RH_ASK rf_driver;
SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  rf_driver.init();
  meuSerial.begin(9600);
  Serial.begin(9600);
}

void loop() {
  if (meuSerial.available() > 0) {
    String mensagemSerial = meuSerial.readStringUntil('\n');
    Serial.println(mensagemSerial);
  }

  uint8_t msg[12];
  uint8_t msglen = sizeof(msg);
  if (rf_driver.recv(msg, &msglen)){
      Serial.println((char*)msg);
  }
}
