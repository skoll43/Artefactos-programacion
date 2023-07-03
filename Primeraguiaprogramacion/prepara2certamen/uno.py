from gpio import *
from time import *

#D2-3 SON LUCES
def apagado():
    digitalWrite(2, LOW)
    digitalWrite(3, LOW)
def prendido():
	digitalWrite(2, HIGH)
	digitalWrite(3, HIGH)
	sleep(1)

#D4-5 ALARMAS HIGH=on LOW=off)
def alarmaon():
	digitalWrite(4,HIGH)
	digitalWrite(5,HIGH)
def alarmaoff():
	digitalWrite(4,LOW)
	digitalWrite(5,LOW)

#D0 LEE alt-mouse (1023) MOVIMIENTO
def detecta():#detectordemovimiento
	if digitalRead(0) == 1023:
		alarmaon()
		prendido()
	if digitalRead(0) == 0:
		alarmaoff()
		apagado()

def sonido():
	if analogRead(A0) > 300:
		alarmaon()
		sleep(5)
		prendido()
		sleep(5)
	if analogRead(A0) < 300:
		alarmaoff()
		apagado()

#D1 digitalWrite(1,0) cerrado
#D1 digitalWrite(1,1) abierto
		
		
def main():

	pinMode(1, OUT)
	print("Prende")
	while True:
		h = localtime()[3]
		m = localtime()[4]
		hora = str(str(h)+":"+str(m))
		detecta()
		sleep(5)
		sonido()
		digitalWrite(1,0) #cierrapuerta
		if hora == "2:0" or (h >= 2 and h < 7):
			customWrite(1,1) #abrepuerta
			prendido()
			sleep(60)
		
		elif h >= 7:
			customWrite(1,0) #cierrapuerta
			sleep(1)
			apagado()
			sleep(1)

if __name__ == "__main__":
	main()