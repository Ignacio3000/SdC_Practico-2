import requests
import json
import convert_int_to_float


# URL de la API REST del Banco Mundial 
base_url = "https://api.worldbank.org/v2/country"

def get_gini_info(country, year):
 #   breakpoint()
    url = f"{base_url}/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    # verificar si la solicitud fue exitosa
    if response.status_code == 200:   # status code 200 para respuestas existosas
        data = response.json()
        return data
    else:
        print("Error en la solicitud:", response.status_code)


#breakpoint()
#convert_int_to_float.convertToFloat(5)
#convert_int_to_float.convertToFloatAsm(5)

gini_info = (get_gini_info("ARG","2010")); 
if gini_info:
    print(f"{gini_info[1][0]['value']}") # toma el primer diccionario del segundo elemento de la lista
gini_info = gini_info[1][0]['value']

int (gini_info);
print(convert_int_to_float.convertToFloatAsm(5));