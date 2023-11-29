#include <RH_ASK.h>
#include <SPI.h>
//Padrão porta 12
RH_ASK rf_driver;

void setup()
{
  rf_driver.init();
}

void loop()
{
  const char *msg = "bc_165_1324_0"; 
  rf_driver.send((uint8_t *)msg, strlen(msg));
  delay(2000);
}