#include <SoftwareSerial.h>
SoftwareSerial HC12(2, 3); // HC-12 TX Pin, HC-12 RX Pin
void setup() {
  Serial.begin(9600);             
  HC12.begin(9600);               
}
void loop() {
  while (HC12.available()) {        
     
    float sensorValue=HC12.read(); 
    Serial.print("CO2= ");
    Serial.print(sensorValue);
    Serial.println("PPM");
    Serial.println(" ");
    delay(1000);
   
    float methane=HC12.read(); 
    Serial.print("CH4= ");
    Serial.print(methane);
    Serial.println("PPM");
    Serial.println(" ");
    delay(1000);
  
    int distance=HC12.read(); 
 
    
    float ax=HC12.read();
    float ay=HC12.read();
    float az=HC12.read();
    float gx=HC12.read();
    float gy=HC12.read();
    float gz=HC12.read();
    
    Serial.print("Accel (g): ");
    Serial.print(ax);
    Serial.print(", ");
    Serial.print(ay);
    Serial.print(", ");
    Serial.println(az);
    delay(1000);

    Serial.print("Gyro (deg/s): ");
    Serial.print(gx);
    Serial.print(", ");
    Serial.print(gy);
    Serial.print(", ");
    Serial.println(gz);
     Serial.println(" ");
    delay(1000);


    
    float temp=HC12.read(); 
    float hum=HC12.read();
    float pres=HC12.read();
    Serial.print("Temperature: ");
    Serial.print(temp);
    Serial.print(" C, Pressure: ");
    Serial.print(pres);
    Serial.print(" Pa, Humidity: ");
    Serial.print(hum);
    Serial.println("% RH");
     Serial.println(" ");
    delay(1000);

  }
    
  }