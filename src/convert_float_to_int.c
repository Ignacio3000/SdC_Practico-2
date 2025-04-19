/*\
 * @file    convert_float_to_int.c
 * @brief   Módulo de extensión en C para Python que convierte flotantes a entero
 *\
 */

#include <Python.h>

/* Declaraciones de funciones externas implementadas en ensamblador */
extern int to_int_asm(float a);
extern int to_int_asm_mil(float b);



/**
 * @brief Convierte un flotante a entero y le suma uno usando C puro.
 *
 * @param numero_float Valor flotante que se convertirá a entero.
 * @return Resultado de la conversión a entero más uno.
 */
int to_int(float numero_float){
    int numero_entero = (int) numero_float;  
    numero_entero = numero_entero + 1;
    return numero_entero;
}



/**
 * @brief Método expuesto a Python que convierte un flotante a entero mediante ensamblador.
 *
 * Recibe un único argumento flotante desde Python, lo convierte a entero
 * sumándole uno y retorna un objeto PyLong.
 *
 * @param self   Referencia al módulo (no usado).
 * @param args   Tupla con los argumentos pasados desde Python.
 * @return PyObject* apuntando al objecto py de tipo float o NULL con excepción.
 */
static PyObject* float_to_int_asm(PyObject* self, PyObject* args){
    float numero_float;
    // Extrae un entero de la tupla de argumentos
    if (!PyArg_ParseTuple(args, "f", &numero_float)) {
        return NULL; // Error: argumento no válido
    }

    int resultado = to_int_asm(numero_float); //Funcion en ASM


    //Se crea un nuevo objeto de Python
    return PyLong_FromLong((long)resultado);
}


/**
 * @brief Método expuesto a Python que convierte un flotante a entero mediante ensamblador y suma
 * 1 mil veces.
 *
 * Recibe un único argumento flotante desde Python, lo convierte a entero
 * sumándole uno mil veces y retorna un objeto PyLong.
 *
 * @param self   Referencia al módulo (no usado).
 * @param args   Tupla con los argumentos pasados desde Python.
 * @return PyObject* apuntando al objecto py de tipo float o NULL con excepción.
 */

static PyObject* float_to_int_asm_mil(PyObject* self, PyObject* args){
    double numero_double;
    // Extrae un entero de la tupla de argumentos
    if (!PyArg_ParseTuple(args, "d", &numero_double)) { //Los numeros decimales de Python son double
        return NULL; // Error: argumento no válido
    }

    int resultado = to_int_asm_mil((float)numero_double); //Funcion en ASM


    //Se crea un nuevo objeto de Python
    return PyLong_FromLong((long)resultado);
}



/**
 * @brief Método expuesto a Python que convierte un float a entero en C puro.
 *
 * Recibe un flotante desde Python, lo convierte a entero sumándole uno
 * y retorna un objeto PyLong.
 *
 * @param self   Referencia al módulo (no usado).
 * @param args   Tupla con los argumentos pasados desde Python.
 * @return PyObject* apuntando al objeto py de tipo int o NULL con excepción.
 */
static PyObject* float_to_int(PyObject* self, PyObject* args) {
    float numero_float;

    // Extrae un float de la tupla de argumentos
    if (!PyArg_ParseTuple(args, "f", &numero_float)) {
        return NULL; // Error: argumento no válido
    }

    int resultado = to_int(numero_float);  // Función en C que hace el cast + 1

    // Devuelve un entero de Python
    return PyLong_FromLong((long)resultado);
}



/**
 * @brief Tabla de métodos exportados por el módulo.
 * 
 *  Cada entrada define:
 * - Nombre del método como será visible desde Python.
 * - Función C que se llamará al invocarlo.
 * - Tipo de argumentos aceptados (METH_VARARGS: recibe tupla de argumentos).
 * - Cadena de documentación del método.
 */
static PyMethodDef convert_float_to_int_Methods[] =
{ 
    {"convertToIntAsm", float_to_int_asm, METH_VARARGS, "Convierte un flotante a entero utilizando ensamblador."},
    {"convertToIntAsmMil", float_to_int_asm_mil, METH_VARARGS, "Convierte un flotante a entero utilizando ensamblador, sumando 1 mil veces."},  
    {"convertToInt", float_to_int, METH_VARARGS, "Convierte un flotante a entero utilizando C puro."},
    {NULL, NULL, 0, NULL} /* Marca el final de la lista */
};


/**
 * @brief Estructura de definición del módulo.
 */
static struct PyModuleDef convertionmod =
{
     PyModuleDef_HEAD_INIT,
     "convert_float_to_int", /* Nombre del módulo */
     "convertir flotante a entero",  /* Documentación del módulo */         
     -1,                         /* Tamaño del estado (módulos sin estado usan -1) */
     convert_float_to_int_Methods  /* Tabla de métodos */
};

/**
 * @brief Punto de inicialización del módulo.
 *
 * Llamado al importar el módulo en Python.
 */
PyMODINIT_FUNC PyInit_convert_float_to_int(void)
{
    return PyModule_Create(&convertionmod);
}




