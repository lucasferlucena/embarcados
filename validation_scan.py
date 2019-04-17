# -*- coding: cp1252 -*-
import blescan
import sys

import bluetooth._bluetooth as bluez

from firebase import firebase

firebase = firebase.FirebaseApplication('https://teste2-943e6.firebaseio.com/')

knownaddress = []

result = firebase.get('/users',None)
for x in range(1, len(result)):
	knownaddress.append(firebase.get('/users',str(x)))

print ("Endereços cadastrados:")

for y in knownaddress:
	print (y)


dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	scanAddress = []
	for x in returnedList:
		#print(x)
		add = str(x).split(",")
		if int(add[5]) >= -70:		
			scanAddress.append(add[0])

	scanAddress = list(dict.fromkeys(scanAddress))

	for beacon in scanAddress:
		if beacon in knownaddress:
			print("LIBERADO", beacon)
		else:
			print("ACESSO NEGADO", beacon)
		
		
##definir um numero de vezes que o scan será executado e quando a lista será atualizada
