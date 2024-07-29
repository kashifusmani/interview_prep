import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GSheetUtil:
    """
    This class is responsible to provide interface to GoogleSheets API
    """

    def __init__(self, sheet_name, credentials_file):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_file, scope
        )
        client = gspread.authorize(credentials)
        sheet = client.open(sheet_name)
        self.worksheet = sheet.get_worksheet(0)

    def get_col_index(self, col_name):
        header_row = self.worksheet.row_values(1)
        return header_row.index(col_name) + 1

    def get_col_values(self, col_index):
        return self.worksheet.col_values(col_index)

    def update_row(self, row_number, col_number, value):
        self.worksheet.update_cell(row_number, col_number, value)
