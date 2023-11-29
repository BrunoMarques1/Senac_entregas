#include <SoftwareSerial.h>
#include <RH_ASK.h>

RH_ASK rf_driver;
SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  rf_driver.init();
  meuSerial.begin(9600);
}

void loop() {
  //const char *msgSerial = "1_165_2000_1";
  //meuSerial.println(msgSerial);
  //delay(500);

  const char *msgRF433 = "x_165_2000_1"; 
  rf_driver.send((uint8_t *)msgRF433, strlen(msgRF433));
  rf_driver.waitPacketSent();
  delay(500);
}
