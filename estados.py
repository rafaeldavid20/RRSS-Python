import sendToDB
import beep
import RPi.GPIO as GPIO
import time
import getFromDB
import estadoEmergencia

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:

	match = 0
	estado = "normal"
        if GPIO.input(13) == False:
                
		beep.pair()
		sendToDB.send("/", "estado" , "alerta")			
		time.sleep (25)
		estado = getFromDB.query("/estado")
		
		if estado == "normal":
			print "vehiculo desbloqueado remotamente"

		if estado == "alerta":
			sendToDB.send("/", "estado" , "emergencia")		
        		estadoEmergencia.emergencia()
			print "vehiculo desbloqueado remotamente"
			estado = getFromDB.query("/estado")		
                
      		
