#include <MPU9250.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#define SEALEVELPRESSURE_HPA (1013.25)
MPU9250 mpu;
Adafruit_BME280 bme;
const int trigPin = 13;
const int echoPin = 12;
long duration;
int distance;
float sensor=A0;
float CH4_value;
float temperature;
float humidity;
float pressure;
float ax,ay,az,gx,gy,gz;

//HC12
SoftwareSerial xbee(2, 3);//xbee tx pin ,xbee rx pin




void setup() {
  Serial.begin(9600);
  xbee.begin(9600); 
  Wire.begin();
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  pinMode(sensor,INPUT);
   
    
    if (!mpu.setup(0x68)) {
    Serial.println("MPU9250 initialization unsuccessful");
    while (1);
  }

if(!bme.begin(0x68)) {
   Serial.println("Could not find a valid BME280 sensor, check wiring!");
   while (1);
  }
}

 
void loop() {

  BME280_readings();
  US_readings();
  MQ5_readings();
  GYRO_readings();

  //xbee
   xbee.write(distance);
   xbee.write(CH4_value);
   xbee.write(temperature);
   xbee.write(humidity);
   xbee.write(pressure);
   xbee.write(ax);
   xbee.write(ay);
   xbee.write(az);
   xbee.write(gx);
   xbee.write(gy);
   xbee.write(gz);
   
}

 
  // BME280 SENSOR
  void BME280_readings(){
   temperature = bme.readTemperature();
   humidity = bme.readHumidity();
   pressure = bme.readPressure()/100.0F;
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
 


  
 // MQ5 METHANE SENSOR
 void MQ5_readings(){
 CH4_value=analogRead(sensor);
 }



// GYROSCOPE
 void GYRO_readings(){
  ax = mpu.getAccX();
  ay = mpu.getAccY();
  az = mpu.getAccZ();
  gx = mpu.getGyroX();
  gy = mpu.getGyroY();
  gz = mpu.getGyroZ();
  }