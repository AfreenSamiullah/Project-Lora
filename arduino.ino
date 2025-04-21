#include <Servo.h>

Servo neckPan, neckTilt;
Servo leftArm, rightArm;

void setup() {
  Serial.begin(115200);
  neckPan.attach(9);
  neckTilt.attach(10);
  leftArm.attach(5);
  rightArm.attach(6);
  neutralPosition();
}

void loop() {
  if(Serial.available() > 0) {
    char cmd = Serial.read();
    switch(cmd) {
      case 'H': happyDance(); break;
      case 'W': wave(); break;
      case 'S': speakAnimation(); break;
    }
  }
}

void happyDance() {
  for(int i=0; i<3; i++) {
    neckPan.write(120);
    leftArm.write(180);
    delay(200);
    neckPan.write(60);
    rightArm.write(0);
    delay(200);
  }
  neutralPosition();
}

void wave() {
  for(int i=0; i<2; i++) {
    rightArm.write(0);
    delay(500);
    rightArm.write(180);
    delay(500);
  }
  neutralPosition();
}

void speakAnimation() {
  for(int i=0; i<3; i++) {
    leftArm.write(60);
    rightArm.write(120);
    delay(150);
    leftArm.write(120);
    rightArm.write(60);
    delay(150);
  }
  neutralPosition();
}

void neutralPosition() {
  neckPan.write(90);
  neckTilt.write(90);
  leftArm.write(90);
  rightArm.write(90);
}
