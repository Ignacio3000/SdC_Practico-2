import convertion_float_to_int
import requests



# URL de la API REST del Banco Mundial 
base_url = "https://api.worldbank.org/v2/country"

def get_gini_info(country, year):
    url = f"{base_url}/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    # verificar si la solicitud fue exitosa
    if response.status_code == 200:   # status code 200 para respuestas existosas
        data = response.json()
        # imprimir la respuesta formateada para una mejor visualización
    #    print(json.dumps(data, indent=2, ensure_ascii=False))
        return data
   # else:
        #print("Error en la solicitud:", response.status_code)

gini_info = get_gini_info("ARG","2020"); 
gini_float = gini_info[1][0]['value']  #guardamos el dato float

#Una sola operacion
#resultado = convertion_float_to_int.convert_and_add_one_time(gini_float)  

for i in range(1000000):
    resultado = convertion_float_to_int.convert_and_add_one_time(gini_float)
       

#Un millon de operaciones
#resultado= convertion_float_to_int.convert_and_add_one_million(gini_float)


print(resultado)
