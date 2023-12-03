#include <RH_ASK.h>
#include <SPI.h>
#include <SoftwareSerial.h>

RH_ASK rf_driver;
SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  rf_driver.init();
  Serial.begin(9600);
  meuSerial.begin(9600);

}

void loop() {
  uint8_t msg[12];
  uint8_t msglen = sizeof(msg);

  if (rf_driver.recv(msg, &msglen)) {
    if (msg[0] == 'b') {
      for (int i = strlen((char*)msg) - 1; i >= 0; i--) {
        if (isdigit(msg[i])) {
          msg[i] = (msg[i] - '0' + 1) % 10 + '0';
          break;
        }
      }
      Serial.println((char*)msg);
      msg[0] = '3';
      meuSerial.println((uint8_t *)msg, strlen(msg));
    } else if (msg[0] == '2') {
        Serial.println((char*)msg);
        for (int i = strlen((char*)msg) - 1; i >= 0; i--) {
          if (isdigit(msg[i])) {
            msg[i] = (msg[i] - '0' + 1) % 10 + '0';
            break;
          }
        }
        msg[0] = '3';
        meuSerial.println((uint8_t *)msg, strlen(msg));
    }
  }
}
