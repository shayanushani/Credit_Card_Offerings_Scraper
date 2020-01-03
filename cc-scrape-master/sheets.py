import gspread
from oauth2client.service_account import ServiceAccountCredentials
import io
import csv

def write_to_google_sheet(data):
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('Credit-Card-Scrape-0266f4350dca.json', scope)

    gc = gspread.authorize(credentials)

    spreadsheet = gc.open_by_url('')


    output = io.StringIO()
    writer = csv.writer(output, delimiter=',')
    writer.writerows(data)
    your_csv_string = output.getvalue()

    gc.import_csv(spreadsheet.id, your_csv_string)

