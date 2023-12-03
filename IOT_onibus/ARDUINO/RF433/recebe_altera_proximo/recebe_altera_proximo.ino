#include <RH_ASK.h>
#include <SPI.h>

RH_ASK rf_driver;

void setup() {
  rf_driver.init();
  Serial.begin(9600);
}

void loop() {
  uint8_t msg[12];
  uint8_t msglen = sizeof(msg);

  if (rf_driver.recv(msg, &msglen)) {
    msg[0] = 'a';

    for (int i = strlen((char*)msg) - 1; i >= 0; i--) {
      if (isdigit(msg[i])) {
        msg[i] = (msg[i] - '0' + 1) % 10 + '0';
        break;
      }
    }

    Serial.println((char*)msg);
  }
}
