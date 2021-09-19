from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = '/home/luke_blue_lox/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dni SARS-CoV-2!A190").execute()
values = result.get('values', [])

RUN1 = [["537", "767","722","652","797","540",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")'],
        
        ["767","722","652","797","540",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")'],
        
        ["722","652","797","540",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")'],
        
        ["652","797","540",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")'],
        
        ["797","540",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")'],
        
        ["540", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B2")'],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!B2")']]
        
request1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni SARS-CoV-2!A190", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dni SARS-CoV-2!M190").execute()
values = result.get('values', [])

RUN11 = [['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2"))', '=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!D2"))'],
        
        ['=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!H2"))','=IF(H:H="","",IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!D2"))']]
        
request11 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni SARS-CoV-2!M190", valueInputOption="USER_ENTERED", body={"values":RUN11}).execute()                                                 
                                                 

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dniowa / 100000!A33").execute()
values = result.get('values', [])

RUN2 = [["1","1","0","0","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")'],
        
        ["1","0","0","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")'],
        
        ["0","0","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C8")'],
        
        ["0","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C8")'],
        
        ["0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C8")'],
        
        ["0", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C8")'],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C8")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C8")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7 / 100000!C8")']]
        
request2 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dniowa / 100000!A33", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dniowa / 100000!L33").execute()
values = result.get('values', [])

RUN3 = [["1","0","0","5","1","1",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")'],
        
        ["0","0","5","1","1",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")'],
        
        ["0","5","1","1",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C29")'],
        
        ["5","1","1",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C29")'],
        
        ["1","1",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C29")'],
        
        ["1", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C29")'],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C29")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7 / 100000!C29")']]
        
request3 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dniowa / 100000!L33", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()
                                                 
                                            
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dniowa / 100000!W33").execute()
values = result.get('values', [])

RUN4 = [["38","37","64","48","43","39",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")'],
        
        ["37","64","48","43","39",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")'],
        
        ["64","48","43","39",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B3")'],
        
        ["48","43","39",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B3")'],
        
        ["43","39",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B3")'],
        
        ["39", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B3")'],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B3")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B3")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!B3")']]
        
request4 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dniowa / 100000!W33", valueInputOption="USER_ENTERED", body={"values":RUN4}).execute()
                                                 
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dniowa / 100000!AH33").execute()
values = result.get('values', [])

RUN5 = [["10","14","15","16","7","17",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")'],
        
        ["14","15","16","7","17",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")'],
        
        ["15","16","7","17",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C31")'],
        
        ["16","7","17",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C31")'],
        
        ["7","17",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C31")'],
        
        ["17", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C31")'],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1 / 100000!C31")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6 / 100000!C31")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7 / 100000!C31")']]
        
request5 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dniowa / 100000!AH33", valueInputOption="USER_ENTERED", body={"values":RUN5}).execute()


print(request1, request11, request2, request3, request4, request5)

# /home/luke_blue_lox/startupscript.sh
