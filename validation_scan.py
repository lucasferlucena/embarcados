# -*- coding: cp1252 -*-
import pyrebase

import blescan
import sys

import bluetooth._bluetooth as bluez

config = {
  }

firebase = pyrebase.initialize_app(config)
#### FORMACAO DA LISTA DE ENDEREÇOS MAC HABILITADOS ####
db = firebase.database()
users = db.child("users").get()

knownaddress = []
for usr in users.each():
    knownaddress.append(usr.val())

for x in knownaddress:
    print(x)

#### FIM ####
#################################################################


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
	print "----------------------------------------"
	for beacon in returnedList:
            ##separar o beacon em partes para comparar somente o enderço mac
            adqaddress = beacon
            if adq_address in knownaddress: 
                knownaddress.index(adq_address)
                print ("ENTRADA PERMITIDA")
            else:
                print ("ENTRADA NEGADA")


