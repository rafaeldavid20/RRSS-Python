import os
import gps
import sendToDB
from time import strftime, gmtime, sleep
import getFromDB

def emergencia():
	
	
	while True:
			
		estado = getFromDB.query("/estado")
		try:
			if estado=="emergencia" and gps.checkForFix():
				latitud, longitud = gps.getCoord()
				coord = str(latitud)+" "+str(longitud)
				timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
				os.system("sudo pon fona")
				sleep(10)
				sendToDB.send("cLocation",timestamp ,coord)
				sendToDB.send("location", "latitud" , latitud)
				sendToDB.send("location", "longitud" , longitud)		
        	        	os.system("sudo poff fona")
				sleep(1)
				break
		except Exception as e:
			print str(e)

		print estado		
		if estado != "emergencia":
			return
