from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import Cliente
import Funciones
import config

SPREADSHEET_ID = config.SPREADSHEET_ID
HOJA = config.HOJA
sheet = Funciones.getSheet()

#Matriz
values = [["pizza"]]
#llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=HOJA+'J2', valueInputOption='USER_ENTERED', body={'values':values}).execute()
# get() obtiene datos de un rango
# update() actualiza en valor de un rango especifico
# append() agrega datos a un rango sin nesecidad de saber donde termina

print("Datos insertados correctamente")
print((result.get('updates').get('updatedCells')))