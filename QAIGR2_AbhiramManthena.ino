void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n'); // Read the message until newline character occurs
    Serial.println(message); // Sends the received message back
  }
}
