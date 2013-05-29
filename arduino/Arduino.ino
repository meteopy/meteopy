######################################################################################
#                                                                                    #
#	Meteopy-project                                                              #
#	Licencia: CreativeCommons (Reconocimiento – NoComercial – CompartirIgual)    #
#	+ INFO= https://github.com/meteopy/meteopy                                   #
#	Contacto desarrollador = @coverantwarrior				     #		     #
#	Twitter oficial del proyecto = @meteopy                                      #
#										     #	
######################################################################################

#include <Wire.h>
#include <Adafruit_BMP085.h>

int LDR_Pin = A10;

Adafruit_BMP085 bmp;

void setup() {
  Serial.begin(9600); 
 
  bmp.begin();
}

void loop() {
  float LDR = analogRead(LDR_Pin);
  float t2 = bmp.readTemperature();
  float p = bmp.readPressure();

    Serial.print("* "); 
    Serial.print(t2);
    Serial.print(" ");
    Serial.print(p/100);
    Serial.print(" ");
    Serial.println(LDR);

}
