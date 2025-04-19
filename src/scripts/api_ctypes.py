import requests
import ctypes


def get_gini_info(country, year):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[1][0]['value']
    else:
        return None

lib = ctypes.CDLL("./build/lib_convertion_ctypes.so") #Cargamos la libreria compartida compilada como libreria dinamica .so

#convert_and_add_one_time es el nombre de la funcion en el .c
lib.convert_and_add_one_time.argtypes = [ctypes.c_float] # Definimos el tipo de argumento de la función
lib.convert_and_add_one_time.restype = ctypes.c_int # Definimos el tipo de retorno de la función
lib.convert_and_add_one_million.argtypes = [ctypes.c_float] # Definimos el tipo de argumento de la función
lib.convert_and_add_one_million.restype = ctypes.c_int # Definimos el tipo de retorno de la función

def convert_and_add(gini_float):
    # Convertimos el float a entero y sumamos 1
    gini_int = lib.convert_and_add_one_time(gini_float) 
    return gini_int 

def convert_and_add_million(gini_float):
    # Convertimos el float a entero y sumamos 1,  un millón de veces
    gini_int = lib.convert_and_add_one_million(gini_float) 
    return gini_int 

def main():
    gini_float = get_gini_info("ARG","2020"); #tomamos el dato de la api
    resultado = convert_and_add(gini_float) 
    print(resultado)
