#include <Servo.h>
#include <cmath>

Servo arm[2][2];
const int arm_pin[2][2]={{l,t},{a1,a2}}; //a1,a2 have l(lift) and t(turn) pins
const int gripper[2][2]={{g11,g12},{g21,g22}}; //gnm, n(motor no.) m(pin no.)
const int misson[2]={{m11,m12},{m21,m22}}; //mpq, p(motor no.) q(pin no.)
const int trigpins[2]={};
const int echopins[2]={};
float durations[2];
float distances[2];

void setup() {
  //initalize and pin setup
  for (int i=0;i<2;i++){
    for (int j=0;j<2;j++){
      arm[i][j].attach(arm_pin[i][j]);
      pinMode(gripper[i][j],OUTPUT);
      pinMode(misson[i][j],OUTPUT);
    }
  }

  for (int i=0;i<2;i++){
    for (int j=0;j<2;j++){
      digitalWrite(gripper[i][j], LOW);
      digitalWrite(misson[i][j], LOW);
    }
  }
  pinMode(trigpins[0],OUTPUT);
  pinMode(trigpins[1],OUTPUT);
  pinMode(trigpins[0],INPUT);
  pinMode(trigpins[1],INPUT);
}

void loop() {
  move(30,45);
  delay(3000);   
}


void drill(misson[2],int arm_no,int x){
  if (x==1){
    digitalWrite(misson[arm_no][0],HIGH);
    digitalWrite(misson[arm_no][1],LOW);
  }
  else if(x==2){
    digitalWrite(misson[arm_no][1],HIGH);
    digitalWrite(misson[arm_no][0],LOW);
  }
  else{
    digitalWrite(misson[arm_no][0],LOW);
    digitalWrite(misson[arm_no][1],LOW);
  }
} 


void lift(Servo arm[2][2],int arm_no, int deg,int pos){
  if(pos==1){
    deg+=0;
  }
  else{
    deg+=90;
  }
  arm[0][arm_no].write(deg);
} 


void turn(Servo arm[2][2],int arm_no,int deg,int pos){
  if(pos==1){
    deg+=0;
  }
  else{
    deg+=90;
  }
  arm[1][arm_no].write(deg);
}

void grip(gripper[2],int arm_no,int x){
  if (x==1){
    digitalWrite(gripper[arm_no][0],HIGH);
    digitalWrite(gripper[arm_no][1],LOW);
  }
  else if(x==2){
    digitalWrite(gripper[arm_no][1],HIGH);
    digitalWrite(gripper[arm_no][0],LOW);
  }
  else{
    digitalWrite(gripper[arm_no][0],LOW);
    digitalWrite(gripper[arm_no][1],LOW);
  }
} 

void getdist(trigpins[2],echopins[2],int arm_no){
  digitalWrite(trigpins[arm_no],LOW);
  delalMicroseconds(2);
  digitalWrite(trigpins[arm_no],HIGH);
  delalMicroseconds(10);
  digitalWrite(trigpins[arm_no],LOW);
  durations[arm_no]=pulseIn(echopins[arm_no],HIGH);
  distances[arm_no]=durations[arm_no]*0.034 /2; 

}


int getdeg(trigpins[2],echopins[2],int arm_no){
  float x,d;
  int deg= ceil(((57.2958*atan(getdist(trigpins,echopins,arm_no))-x)/d) + ((57.2958*atan(getdist(trigpins,echopins,arm_no))-x)/d))
  return deg;
}

void move(int d1, int d2){
  grip(gripper,0,1);
  lift(arm,0,d1,1);
  delay(1000);
  turn(arm,0,d2,1);
  delay(1000);
  lift(arm,0,d1,0);
  delay(1000);
  grip(gripper,0,0);

  grip(gripper,1,1);
  lift(arm,1,d1,1);
  delay(1000);
  turn(arm,0,0,0);
  delay(1000);
  turn(arm,1,d2,1);
  delay(1000);
  lift(arm,1,d1,0);
  delay(1000);
  grip(gripper,1,0);
}

