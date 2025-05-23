import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def uploadtoworksheet(new_row):

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    creds = Credentials.from_service_account_file("Credentials.json",
                                              scopes = scopes)
    client = gspread.authorize(creds)

    sheetsid = "SheetsID" #from the url of google sheeets
    sheetname = "Database" #exact name of the database

    sheet = client.open_by_key(sheetsid)
    worksheet = sheet.worksheet(sheetname)
    header = worksheet.row_values(1)

    ordered_row = [new_row.iloc[0].get(col, "") for col in header]
    worksheet.append_row(ordered_row)


new_row = pd.DataFrame([{
    "ID": "job_ID",
    "NAME": "job_title",
    "COMPANY NAME": "companyname",
    "LINK": "apply_link",
    "RESUME ID": "resume_id",
    "SCRAPED DATE": "today",
    "DESCRIPTION": "job_desc"
        }])

uploadtoworksheet(new_row)
