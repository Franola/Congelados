from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from Cliente import Cliente
import Funciones
import config

def agregarPedido(nombreCliente, pedido):
    SPREADSHEET_ID = config.SPREADSHEET_ID
    HOJA = config.HOJA
    sheet = Funciones.getSheet()

    #pedido = [["Arvejas", "1"], ["Moras", "1"], ["Acelga", "1"]]
    #pedido = [[congelados, cantidad]]
    cliente = Cliente([[nombreCliente]], pedido)

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=HOJA+'C2:C100').execute()
    datos = result.get('values', [])

    #print(datos)
    fila = len(datos) + 2
    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, 
                                range=HOJA+'A'+str(fila), 
                                valueInputOption='USER_ENTERED', 
                                body={'values':cliente.nombre}).execute()

    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, 
                                range=HOJA+'C'+str(fila), 
                                valueInputOption='USER_ENTERED', 
                                body={'values':cliente.pedido}).execute()

    for i in cliente.pedido:
        fila+=1
        
    #fila+=1
    result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, 
                                range=HOJA+'C'+str(fila), 
                                valueInputOption='USER_ENTERED', 
                                body={'values':[["TOTAL"]]}).execute()


    #Matriz
    #values = [["Frutillas", "1"]]
    #llamamos a la api
    #result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, 
    #                               range=HOJA+'C15', 
    #                               valueInputOption='USER_ENTERED', 
    #                               body={'values':values}).execute()

    return 'Pedido insertados correctamente'
    #print((result.get('updates').get('updatedCells')))

"""
nombre = "Bruno"
pedido = "Zapallo"
cant = "3"
res = agregarPedido(nombreCliente=nombre, congelados=pedido, cantidad=cant)
print(res)
"""

