#include <ESP32Servo.h>
#include "esp_camera.h"

#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"

Servo pan, tilt;
int panAngle = 90, tiltAngle = 90;

void setup() {
  Serial.begin(115200);
  pan.attach(12);
  tilt.attach(13);
  
  camera_config_t config = {
    .pin_pwdn = 32, .pin_reset = -1,
    .pin_xclk = 0, .pin_sscb_sda = 26,
    .pin_sscb_scl = 27, .pin_d7 = 35,
    .pin_d6 = 34, .pin_d5 = 39,
    .pin_d4 = 36, .pin_d3 = 21,
    .pin_d2 = 19, .pin_d1 = 18,
    .pin_d0 = 5, .pin_vsync = 25,
    .pin_href = 23, .pin_pclk = 22,
    .xclk_freq_hz = 20000000,
    .pixel_format = PIXFORMAT_JPEG,
    .frame_size = FRAMESIZE_QVGA,
    .jpeg_quality = 12,
    .fb_count = 1
  };
  
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) Serial.println("Camera Init Failed");
}

void loop() {
  camera_fb_t *fb = esp_camera_fb_get();
  if(!fb) return;

  // Face detection logic (pseudo-code)
  int faceX = detectFaceX(fb->buf);
  int faceY = detectFaceY(fb->buf);
  
  panAngle = constrain(panAngle + map(faceX, 0, 320, -2, 2), 0, 180);
  tiltAngle = constrain(tiltAngle + map(faceY, 0, 240, -2, 2), 0, 180);
  
  pan.write(panAngle);
  tilt.write(tiltAngle);
  
  esp_camera_fb_return(fb);
  delay(50);
}
