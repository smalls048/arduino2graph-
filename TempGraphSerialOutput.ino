#include <DHT.h>
#define DHTpin 2
#define DHTtype DHT22
DHT dht(DHTpin, DHTtype);
void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);
  float temp = dht.readTemperature();
  Serial.println(temp);

}
