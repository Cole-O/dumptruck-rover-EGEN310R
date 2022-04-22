#include <Servo.h>
char t;
Servo dumpServo;
 
void setup() {
//Pin initialize
pinMode(13,OUTPUT);   //left motors forward
pinMode(12,OUTPUT);   //left motors reverse
pinMode(11,OUTPUT);   //right motors forward
pinMode(10,OUTPUT);   //right motors reverse
pinMode(9,OUTPUT);   //Servo
Serial.begin(9600);

//Servo Setup
dumpServo.attach(9); //attach servo and tell what pin numbers it is on
dumpServo.writeMicroseconds(1500);
}
 
void loop() {
if(Serial.available()){
  t = Serial.read();
  Serial.println(t);
  Serial.write('R');  //Testing latency Remove Later, could add before digitalWrites
}
 
if(t == 'w' || t == 'W'){            //move forward(all motors rotate in forward direction)
  digitalWrite(13,HIGH);
  digitalWrite(11,HIGH);
}
 
else if(t == 's' || t == 'S'){      //move reverse (all motors rotate in reverse direction)
  digitalWrite(12,HIGH);
  digitalWrite(10,HIGH);
}
 
else if(t == 'd' || t == 'D'){      //turn right (left side motors rotate in forward direction, right side motors doesn't rotate)
  digitalWrite(11,HIGH);
}
 
else if(t == 'a' || t == 'A'){      //turn left (right side motors rotate in forward direction, left side motors doesn't rotate)
  digitalWrite(13,HIGH);
}

else if(t == 'l'){
//Dump bed down
dumpServo.writeMicroseconds(1300);
}
else if(t == 'L'){
//Dump bed up
dumpServo.writeMicroseconds(1700);
}
 
else if(t == ' '){      //STOP (all motors and servo stop)
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  digitalWrite(10,LOW);
  dumpServo.writeMicroseconds(1500);
}
delay(100);
}
