import serial
from time import sleep

def checkForFix():
	print "checking for fix"
	ser=serial.Serial('/dev/ttyS0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	ser.write("AT+CGNSPWR=1\r")
	ser.write("AT+CGNSPWR?\r")
	while True:
		response = ser.readline()
		if " 1" in response:
			break
	ser.write("AT+CGNSINF\r")
	while True:
			response = ser.readline()
			if "+CGNSINF: 1,1," in response:
				print "fix found"
				print response
				return True
			if "+CGNSINF: 1,0," in response:
				sleep(5)
				ser.write("AT+CGNSINF\r")
				print "still looking for fix"	
			else:
				ser.write("AT+CGNSINF\r")
				return

def getCoord():
	ser=serial.Serial('/dev/ttyS0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
	ser.write("AT+CGNSINF\r")
	while True:
		response = ser.readline()
		if "+CGNSINF: 1," in response:
			array = response.split(",")
			lat = array[3]
			print lat
			lon = array[4]
			print lon
			return (lat,lon)

