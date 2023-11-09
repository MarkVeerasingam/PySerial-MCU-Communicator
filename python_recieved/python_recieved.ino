#define MAX_BUFF_LEN 255

char c;
char str[MAX_BUFF_LEN];
uint8_t idx = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if(Serial.available() > 0){
    c = Serial.read(); //read 1 byte
    
    if(c != '\n'){ //still reading
      str[idx++] = c; // Parse the string byte (char) by byte
    } 
    else{ //done reading
      str[idx] = '\0'; // convert it to a string
      idx = 0;

      Serial.print("Recieved: ");
      Serial.println(str);
    }
  }
}
