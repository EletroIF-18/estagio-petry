double valorLido;
uint16_t valorMedio;
bool valorChaveamento;

void setup(){
  Serial.begin(115200);
}

void loop(){
  valorLido = analogRead(A0);
  valorMedio = analogRead(A1);
  valorLido = ((valorLido - valorMedio/2) * 5)/1023;
  analogRead(A2) >= 100 ? valorChaveamento=true : valorChaveamento=false;



  
  //Serial.println(valorChaveamento);
  //Serial.println(valorLido);
}
