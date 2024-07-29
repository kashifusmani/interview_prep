import requests
from json import loads
from converters import celsius_to_fahrenheit, kmh_to_mph, get_current_time_pst
from gsheet_util import GSheetUtil

"""
This is the main runner class that implements the business logic
"""


def populate_sheet(sheet_name, credentials_file_path):
    worksheet = GSheetUtil(sheet_name, credentials_file_path)
    lat_index = worksheet.get_col_index("Latitude")
    lon_index = worksheet.get_col_index("Longitude")

    latitude_values = worksheet.get_col_values(lat_index)
    longitude_values = worksheet.get_col_values(lon_index)

    data_tuples = list(zip(latitude_values[1:], longitude_values[1:]))

    update_row_number = 2
    temp_index = worksheet.get_col_index("Current Temperature")
    wind_speed_index = worksheet.get_col_index("Current Wind Speed")
    last_updated_time_index = worksheet.get_col_index("Last Updated Time (in PST)")

    for lat, lon in data_tuples:
        try:
            resp = requests.get(
                "https://api.open-meteo.com/v1/forecast?latitude="
                + lat
                + "&longitude="
                + lon
                + "&current=temperature,wind_speed_10m"
            )
            if resp.status_code == 200:
                data = loads(resp.content)
                temperature = data["current"]["temperature"]
                wind_speed = data["current"]["wind_speed_10m"]
                print(temperature)
                print(wind_speed)
                print("=====")
                # scrape_time = data['current']['time']

                worksheet.update_row(
                    update_row_number,
                    temp_index,
                    str(celsius_to_fahrenheit(temperature)) + " F",
                )
                worksheet.update_row(
                    update_row_number,
                    wind_speed_index,
                    str(kmh_to_mph(wind_speed)) + " mph",
                )
                # worksheet.update_cell(row_number, last_updated_time_index, convert_utc_to_pst(str_to_date(scrape_time)))
                worksheet.update_row(
                    update_row_number, last_updated_time_index, get_current_time_pst()
                )
            else:
                print("something went wrong " + str(resp))
        except Exception as e:
            print(e)
        update_row_number += 1


if __name__ == "__main__":
    sheet_name = "Acryl Weather Data Take Home"
    credentials_file_path = "acryl-data-417621-5a0cf944cb64.json"
    populate_sheet(sheet_name, credentials_file_path)
