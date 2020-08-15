import gspread
def on_colab(gspread_url, sheet_name):
    from google.colab import auth
    from oauth2client.client import GoogleCredentials
    auth.authenticate_user()
    credentials = GoogleCredentials.get_application_default()
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(gspread_url)
    worksheet = sheet.worksheet(sheet_name)
    return worksheet.get_all_values()

def on_local(json_file, gspread_url, sheet_name):
    from oauth2client.service_account import ServiceAccountCredentials
    import gspread
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(gspread_url)
    worksheet = sheet.worksheet(sheet_name)
    return worksheet.get_all_values()

if __name__ == "__main__":
    json_file="credentials.json"
    gspread_url = "https://docs.google.com/spreadsheets/d/1ycm7PmZAhL-gb2Zt9BmNx2RN_pJYD4-5w4D7JM28y3s/edit#gid=478056099"
    sheet_name = "Form Responses 1"
    sheet_data = on_local(json_file=json_file, gspread_url=gspread_url, sheet_name=sheet_name)
    columns = sheet_data[0]
    data = sheet_data[1:]
    print(columns, data)