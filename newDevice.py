from bluetooth import *
from bluetool import Bluetooth
import getMAC
import btConnect
import beep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

MACs = getMAC.query("RR").values()

while True:

	match = 0

        if GPIO.input(13) == False:
                
		beep.pair()

                print "Performing inquiry..."

                nearby_devices = discover_devices(lookup_names = True)

                print "Found %d devices" % len(nearby_devices)
		
                for addr, name in nearby_devices:
	
			for k in range(len(MACs)):
		
				if MACs[k] == addr:
					match = match + 1 
					beep.match()
					port = btConnect.connect(MACs[k])
                                        print "MAC: " +  addr + " found on DB"
					print "RRSS service port: " + str(port)				
					print "Pairing..."
					Pair = Bluetooth()
					print Pair.pair(addr)
				
      		if match == 0:
		
			beep.noMatch()
