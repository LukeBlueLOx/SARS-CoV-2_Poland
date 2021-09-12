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
                            range="Średnia 7 dni - Zakres 2 tygodnie!B3").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!H168:H181")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I168:I181")']]

request1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni - Zakres 2 tygodnie!B3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dni - Zakres 4 tygodnie!B3").execute()
values = result.get('values', [])

RUN2 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!H154:H181")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!I154:I181")']]

request2 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni - Zakres 4 tygodnie!B3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Prognoza liczby zgonów - 21 dni do przodu!B3").execute()
values = result.get('values', [])

RUN3 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!O161:O181")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dni SARS-CoV-2!P161:P181")']]

request3 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Prognoza liczby zgonów - 21 dni do przodu!B3", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()                                                


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Karkonoski!B2").execute()
values = result.get('values', [])

RUN4 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!I11:I24")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!K11:K24")']]

request4 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Karkonoski!B2", valueInputOption="USER_ENTERED", body={"values":RUN4}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Karkonoski 28 dni!B2").execute()
values = result.get('values', [])

RUN41 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!I2:I29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!K2:K29")']]

request41 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Karkonoski 28 dni!B2", valueInputOption="USER_ENTERED", body={"values":RUN41}).execute()                             


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Jelenia Góra!B2").execute()
values = result.get('values', [])

RUN5 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!T11:T24")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!V11:V24")']]

request5 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Jelenia Góra!B2", valueInputOption="USER_ENTERED", body={"values":RUN5}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Jelenia Góra 28 dni!B2").execute()
values = result.get('values', [])

RUN51 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!T2:T29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!V2:V29")']]

request51 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Jelenia Góra 28 dni!B2", valueInputOption="USER_ENTERED", body={"values":RUN51}).execute()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Dolnośląskie!B2").execute()
values = result.get('values', [])

RUN6 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AE11:AE24")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AG11:Ag24")']]

request6 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Dolnośląskie!B2", valueInputOption="USER_ENTERED", body={"values":RUN6}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Dolnośląskie 28 dni!B2").execute()
values = result.get('values', [])

RUN61 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AE2:AE29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AG2:AG29")']]

request61 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Dolnośląskie 28 dni!B2", valueInputOption="USER_ENTERED", body={"values":RUN61}).execute()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Wrocław!B2").execute()
values = result.get('values', [])

RUN7 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AP11:AP24")', '=IMPORTRANGE("1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AR11:AR24")']]

request7 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Wrocław!B2", valueInputOption="USER_ENTERED", body={"values":RUN7}).execute()
                                                 
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Wrocław 28 dni!B2").execute()
values = result.get('values', [])

RUN71 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AP2:AP29")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM","Średnia 7 dniowa / 100000!AR2:AR29")']]

request71 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Wrocław 28 dni!B2", valueInputOption="USER_ENTERED", body={"values":RUN71}).execute()

print(request1, request2, request3, request4, request41, request5, request51, request6, request61, request7, request71)

# /home/luke_blue_lox/startupscript.sh
