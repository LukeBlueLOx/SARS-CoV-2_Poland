f = open ("/home/luke_green_player/Downloads/Repeat/test.py", "r+")
f.write ('''from googleapiclient.discovery import build\nfrom google.oauth2 import service_account\n\nSERVICE_ACCOUNT_FILE = '/home/luke_green_player/Downloads/Repeat/sars-cov-2-poland.json'\nSCOPES = ['https://www.googleapis.com/auth/spreadsheets']\n\nRUN1 = [['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1ys-rIwopVtp_PDzr4tV_ycF1z1Vfug54BJ0IUVx1SNs","Średnia 7 dni SARS-CoV-2!H168:H181")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1ys-rIwopVtp_PDzr4tV_ycF1z1Vfug54BJ0IUVx1SNs","Średnia 7 dni SARS-CoV-2!I168:I181")']]\n\nrequest1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,\n
                                                 range="Średnia 7 dni - Zakres 2 tygodnie!B3", valueInputOption="USER_ENTERED",\nbody={"values":RUN1}).execute()\n

print(request1)''')
f.close
#inkrementacja
