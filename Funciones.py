from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import Cliente
import config

def getSheet():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] 
    KEY = 'key.json'

    # Escribe aquí el ID de tu documento:
    SPREADSHEET_ID = config.SPREADSHEET_ID

    creds = None
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    return sheet