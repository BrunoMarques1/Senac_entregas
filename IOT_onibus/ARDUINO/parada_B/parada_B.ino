#include <SoftwareSerial.h>
#include <RH_ASK.h>

RH_ASK rf_driver;
SoftwareSerial meuSerial(2, 3); // RX, TX

void setup() {
  meuSerial.begin(9600);
  Serial.begin(9600);
  rf_driver.init();
}

void loop() {
  // Comunicação entre paradas
  if (meuSerial.available() > 0) {
    String mensagemSerial = meuSerial.readStringUntil('\n');
    if (mensagemSerial.substring(0, 2) == "p2"){ // Index parada
      Serial.println(mensagemSerial); // Manda para o python
      mensagemSerial[1] = '3'; // Prepara para proxima parada
      for (int i = mensagemSerial.length() - 1; i >= 0; i--) { // Adiciona distancia
        if (isdigit(mensagemSerial[i])) {
          mensagemSerial[i] = mensagemSerial[i] + 1;
          break;
        }
      }
      meuSerial.println(mensagemSerial); // Manda para proxima parada
    }
  }

  // Onibus
  uint8_t msg[13];
  uint8_t msglen = sizeof(msg);
  if (rf_driver.recv(msg, &msglen)) {
    if (msg[0] == 'b' && msg[1] == 'c') {
      for (int i = msglen - 1; i >= 0; i--) {
        if (isdigit(msg[i])) {
          msg[i] = msg[i] + 1;
          break;
        }
      }

      // Prepara para o python
      msg[0] = 'p';
      msg[1] = 'b';
      Serial.println(String((char*)msg)); // Manda para o python
      msg[1] = '3'; // Prepara para proxima parada
      meuSerial.println(String((char*)msg)); // Manda para proxima parada
    }
  }
}
