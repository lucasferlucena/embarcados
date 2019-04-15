# -*- coding: cp1252 -*-
import pyrebase

config = {
    "apiKey": "AIzaSyARBceJ3lWLFDGVoQ1VfUtY4GXXzsyVPDI",
    "authDomain": "teste2-943e6.firebaseapp.com",
    "databaseURL": "https://teste2-943e6.firebaseio.com",
    "projectId": "teste2-943e6",
    "storageBucket": "teste2-943e6.appspot.com",
    "messagingSenderId": "808394656425"
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

#### CHECAGEM SE O ENDEREÇO OBTIDO ESTA NA LISTA ####

#adqaddress = ##TODO

#if adq_address in knownaddress:
#    knownaddress.index(adq_address)
#    print ("ENTRADA PERMITIDA")
#else:
#    print ("ENTRADA NEGADA")

if knownaddress.index("23a"):
    print ("opa")
else:
    print("oi")
