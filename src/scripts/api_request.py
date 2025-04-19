
import requests
import convert_int_to_float

def get_gini_info(country, year):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[1][0]['value']
    else:
        return None

def main():
    gini_info = get_gini_info("ARG", "2010")
    if gini_info:
      print(  convert_int_to_float.convertToFloatAsm(int(gini_info)) )

main()

