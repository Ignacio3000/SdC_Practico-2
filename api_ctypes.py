import requests
import ctypes


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


lib = ctypes.CDLL("./lib_convertion_ctypes.so") #Cargamos la libreria compartida compilada como libreria dinamica .so

#convert_and_add_one_time es el nombre de la funcion en el .c
lib.convert_and_add_one_time.argtypes = [ctypes.c_float] # Definimos el tipo de argumento de la función
lib.convert_and_add_one_time.restype = ctypes.c_int # Definimos el tipo de retorno de la función
lib.convert_and_add_one_million.argtypes = [ctypes.c_float] # Definimos el tipo de argumento de la función
lib.convert_and_add_one_million.restype = ctypes.c_int # Definimos el tipo de retorno de la función


gini_info = get_gini_info("ARG","2020"); 
gini_float = gini_info[1][0]['value']  #guardamos el dato float


#Conversion de float a entero +1, con ctypes una sola vez
#resultado = lib.convert_and_add_one_time(gini_float) #llamamos a la funcion de la libreria compartida

#Conversion de float a entero +1, con ctypes un millon de veces
resultado = lib.convert_and_add_one_million(gini_float) #llamamos a la funcion de la libreria compartida

print(resultado)
