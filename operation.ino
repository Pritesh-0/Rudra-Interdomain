#include <Servo.h>

Servo arm[2][2];
const int arm_pin[2][2]={{p1,p2},{p3,p4}};

void setup() {
  for (int i=0;i<2;i++){
    for (int j=0;j<2;j++){
      arm[i][j].attach(arm_pin[i][j])
    }
  }
}

void loop() {
  move(30,45);
  delay(3000);   
}



void lift(Servo arm[2][2],int arm_no, int deg,char x){
  switch(x){
    case 'u':
      deg+=0;
      break;
    case 'd':
      deg+=90;
      break;
  }
  arm[0][arm_no].write(deg);
} 


void turn(Servo arm[2][2],int deg,char x){
  switch(x){
    case 'r':
      deg+=0;
      break;
    case 'l':
      deg+=90;
      break;
  }
  arm[0][arm_no].write(deg);
}


void move(int d1, int d2){
  //touch(arm1_claw,1)
  lift(arm,0,d1,'u');
  delay(1000);
  turn(arm,0,d2,'r');
  delay(1000);
  lift(arm,0,d1,'d');
  delay(1000);
  //touch(arm1_claw,0);

  //touch(arm2_claw,1);
  lift(arm,1,d1,'u');
  delay(1000);
  turn(arm,0,0,'l');
  delay(1000);
  turn(arm,1,d2,'r');
  delay(1000);
  lift(arm,1,d1,'d');
  delay(1000);
  //touch(arm2_claw,0);
}