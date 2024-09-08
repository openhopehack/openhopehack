import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from flask import current_app


class Google:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self, spreadsheet_id, range_name, service_account_file_name):
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        service_account_file_name = os.path.join(
            current_app.root_path, service_account_file_name
        )
        with open(service_account_file_name, "r") as file:
            service_account_info = json.load(file)
        creds = Credentials.from_service_account_info(
            service_account_info, scopes=self.SCOPES
        )
        self.service = build("sheets", "v4", credentials=creds)

    def append_to_sheet(self, values):
        body = {"values": values}
        result = (
            self.service.spreadsheets()
            .values()
            .append(
                spreadsheetId=self.spreadsheet_id,
                range=self.range_name,
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        return result.get("updates").get("updatedCells")
