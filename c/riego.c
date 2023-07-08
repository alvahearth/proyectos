#include <LiquidCrystal.h>
LiquidCrystal lcd(11,10,9,8,7,6);

const int pot=0;
int humedad;

float tempC;
int pinLM35 = 1;

int pinLDR = 2;
int luzLDR = 0;

void setup() {
lcd.begin(16,2);

Serial.begin(9600);
pinMode(4,OUTPUT);
pinMode(3,OUTPUT);
pinMode(2,OUTPUT);
}

void loop() {
humedad = analogRead (pot) / 10;
tempC = analogRead(pinLM33);

tempC = (1.1 * tempC * 100.0)/1024.0;
luzLDR= analogRead(pinLDR);

if((humedad<65)&&(tempC>=28)){
digitalWrite(2, HIGH);
digitalWrite(3, HIGH);

if(luzLDR<150){
digitalWrite(4,HIGH);
} else{digitalWrite(4,LOW);}

}
else if((humedad<65)&&(tempC<28)){
digitalWrite(2, HIGH);
digitalWrite(3, LOW);
if(luzLDR<150){
digitalWrite(4,HIGH);
} else{digitalWrite(4,LOW);}
}
else if((humedad>=65)&&(tempC>=28)){
digitalWrite(2, LOW);
digitalWrite(3, HIGH);

if(luzLDR<150){
digitalWrite(4,HIGH);
} else{digitalWrite(4,LOW);}
}
else{
digitalWrite(2, LOW);
digitalWrite(3,LOW);
if(luzLDR<150){

digitalWrite(4,HIGH);
} else{digitalWrite(4,LOW);}
}
lcd.setCursor(0,0);
lcd.print("Temp:");
lcd.print(" Humedad:");
lcd.setCursor(0,1);
lcd.print(tempC);
lcd.println(" C ");
lcd.print(humedad);
lcd.println(" % ");
}
