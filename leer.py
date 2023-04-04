from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import Cliente
import Funciones
import config

SPREADSHEET_ID = config.SPREADSHEET_ID
HOJA = config.HOJA
sheet = Funciones.getSheet()


result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=HOJA+'K55:L55').execute()

totales = result.get('values', [])
Ganancia = totales[0][1]

print("Ganancia total: ", Ganancia)

#print(totales[0])
#print("Ganancia total: " + Ganancia)

#result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=config.HOJA+'L6:M25').execute()
#totales = result.get('values', [])
#print(totales)

"""
cliente = Cliente()
cont = 0
for i in clientes:
    if i!='':
        cont += 1
        if i == 'pepe':
            numCli = cont

cliente.nro = numCli

cont = 0
for i in elementos:
    if i == 'TOTAL':
        cont += 1
        
"""
