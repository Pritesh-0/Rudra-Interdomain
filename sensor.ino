#include <SoftwareSerial.h>
#include <BME280I2C.h>
#include <Wire.h>
BME280I2C bme;
#include <MPU6050.h>
MPU6050 mpu;
float sensorValue=A1;
float Msensor=A0;
float ch4;
float co2;
int trigPin = 12;
int echoPin = 10;
long duration;
long distance;
float temp(NAN), hum(NAN), pres(NAN);
int16_t ax, ay, az;
int16_t gx, gy, gz;

SoftwareSerial HC12(2, 3); // HC-12 TX Pin, HC-12 RX Pin

  void setup() {
  Serial.begin(9600); 
  while(!Serial) {} // Wait
  Wire.begin();

  while(!bme.begin())
  {
    Serial.println("Could not find BME280 sensor!");
    delay(1000);
  }

  switch(bme.chipModel())
  {
     case BME280::ChipModel_BME280:
       Serial.println("Found BME280 sensor! Success.");
       break;
     case BME280::ChipModel_BMP280:
     Serial.println("Found BME280 sensor! No Humidity available.");
       break;
     default:
       Serial.println("Found UNKNOWN sensor! Error!");
  }
  
   mpu.initialize();// Serial port to computer
   HC12.begin(9600);               // Serial port to HC12
   pinMode(trigPin, OUTPUT); 
   pinMode(echoPin, INPUT); 
}



void loop() {
  
  
 //bme 
   BME280Data();
   HC12.print(temp);
   HC12.print(pres);
   HC12.print(hum);
   delay(1000);


   
   
  //mq5
    MQ5_readings();
    HC12.print(sensorValue);
    delay(1000);



 
    //mq135
      MQ135_readings();
      HC12.print(Msensor);
      delay(1000); 



      //US
      US_readings();
      HC12.print(distance);
      delay(1000);



   //mpu
    mpu_readings();
    HC12.print('ax');
    HC12.print(ax);
    HC12.print(ay);
    HC12.print(az);
    HC12.print(gx);
    HC12.print(gy);
    HC12.print(gz);
    delay(1000);
}   



// //MQ5 METHANE SENSOR
  void MQ5_readings(){
  ch4=analogRead(Msensor);
}


 
// //MQ135 c02 SENSOR
  void MQ135_readings(){
  co2=analogRead(sensorValue);
 }



 
 // ultrasonic sensor
   void US_readings(){
   digitalWrite(trigPin, LOW);
   delayMicroseconds(2);
   digitalWrite(trigPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(trigPin, LOW);
   duration = pulseIn(echoPin, HIGH);
   distance = duration * 0.034 / 2;
}





//  //Bme280 SENSOR
    void BME280Data()
{
    bme.read(temp,pres,hum);

}




   
//   //mpu
   void mpu_readings(){
   mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
   float axg = (float)ax / 16384.0;
   float ayg = (float)ay / 16384.0;
   float azg = (float)az / 16384.0;
   float gxds = (float)gx / 131.0;
   float gyds = (float)gy / 131.0;
   float gzds = (float)gz / 131.0;
   
 }