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
  lift(arm1_lift,45,'u');
}



void lift(Servo arm[2][2],int arm_no, int deg,char x){
  switch(x){
    case 'u':
      deg+=90;
      break;
    case 'd':
      deg-90;
      break;
  }
  arm[0][arm_no].write(deg);
} 


void turn(Servo arm[2][2],int deg,char x){
  switch(x){
    case 'r':
      deg+=90;
      break;
    case 'l':
      deg-=90;
      break;
  }
  arm[0][arm_no].write(deg);
}


void move(int d1, int d2){
  touch(arm1_claw,1)
  lift(arm,1,d1,'u');
  turn(arm,1,d2,'r');
  lift(arm,1,d1,'d');
  touch(arm1_claw,0);

  touch(arm2_claw,1);
  lift(arm,2,d1,'u');
  turn(arm,2,d2,'r');
  lift(arm,2,d1,'d');
  touch(arm2_claw,0);
}