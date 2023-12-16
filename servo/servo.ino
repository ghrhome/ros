#include <Servo.h>
int led4=4;       
 
int led=13;         
Servo myservo;//创建舵机对象
 
void setup(){
  myservo.attach(9, 500, 2500);
  pinMode(led,OUTPUT);
  pinMode(led4,OUTPUT);
  Serial.begin(9600);
}
 
void loop(){
  if(Serial.available()>0){
    char c=Serial.read();
    if(c=='2'){
      digitalWrite(led,HIGH);
      digitalWrite(led4,HIGH);
      myservo.write(90);
      Serial.println("ON");
    }
     else if(c=='4'){
      digitalWrite(led,LOW);
      digitalWrite(led4,LOW);
      myservo.write(180);
      Serial.println("OFF");
    }
  }
}
