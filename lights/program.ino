#define RED 13
#define YELLOW 12
#define GREEN 11

void setup() {                
  // initialize the digital pin13 as an output.
  pinMode(RED, OUTPUT);     
  pinMode(YELLOW, OUTPUT);     
  pinMode(GREEN, OUTPUT);  
       
  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, LOW);  
}

void loop() {
  digitalWrite(RED, HIGH);
  delay(5000);

  digitalWrite(RED, LOW);
  digitalWrite(YELLOW, HIGH);
  delay(2000);

  digitalWrite(YELLOW, LOW);
  digitalWrite(GREEN, HIGH);
    
  delay(5000);

  digitalWrite(GREEN, LOW);
  delay(500);
      
  digitalWrite(GREEN, HIGH);
  delay(500);  

  digitalWrite(GREEN, LOW);
  delay(500);
      
  digitalWrite(GREEN, HIGH);
  delay(500);  

  digitalWrite(GREEN, LOW);
  delay(500);
      
  digitalWrite(GREEN, HIGH);
  delay(500);

  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, HIGH);
  
  delay(2000);
  
  digitalWrite(YELLOW, LOW);
}