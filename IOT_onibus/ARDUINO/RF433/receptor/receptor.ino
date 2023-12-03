#include <RH_ASK.h>
#include <SPI.h>
//Porta padrão 11
RH_ASK rf_driver;

void setup()
{
  rf_driver.init();
  Serial.begin(9600);
}

void loop()
{
  uint8_t buf[13];
  uint8_t buflen = sizeof(buf);

  if (rf_driver.recv(buf, &buflen)){
    Serial.println((char*)buf);
  }
}
