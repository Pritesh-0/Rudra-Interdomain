#include <Servo.h>

Servo arm[2][2];
const int arm_pin[2][2]={{8,9},{10,11}};
const int gripper[2]={6,7};

void setup() {
  for (int i=0;i<2;i++){
    for (int j=0;j<2;j++){
      arm[i][j].attach(arm_pin[i][j]);
    }
  }
}

void loop() {
  move(30,45);
  delay(3000);   
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
  if (x){
    digitalWrite(gripper[arm_no],HIGH);
  }
  else{
    digitalWrite(gripper[arm_no],LOW);
  }
} 


void move(int d1, int d2){
  //touch(arm1_claw,1)
  lift(arm,0,d1,1);
  delay(1000);
  turn(arm,0,d2,1);
  delay(1000);
  lift(arm,0,d1,0);
  delay(1000);
  //touch(arm1_claw,0);

  //touch(arm2_claw,1);
  lift(arm,1,d1,1);
  delay(1000);
  turn(arm,0,0,0);
  delay(1000);
  turn(arm,1,d2,1);
  delay(1000);
  lift(arm,1,d1,0);
  delay(1000);
  //touch(arm2_claw,0);
}

