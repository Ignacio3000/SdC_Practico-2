/*\
 * @file    convert_int_to_float.c
 * @brief   Módulo de extensión en C para Python que convierte enteros a flotante
 *\
 */

#include <Python.h>

/* Declaraciones de funciones externas implementadas en ensamblador */
extern float adder(int a, int b);
extern float convert_to_float(int a);

/**
 * @brief Convierte un entero a flotante y le suma diez usando funciones en ensamblador.
 *
 * Esta funcion llama a una subrutina externa en assembler, reailiza una conversion de 
 * entero a flotante y una adicion.
 *
 * @param numero_entero Valor entero que se convertirá a float.
 * @return Resultado de la conversión a float más diez.
 */
float to_float_asm(int numero_entero){
    float numero_flotante = convert_to_float(numero_entero);
    numero_flotante = adder(numero_entero,10);    
    return numero_flotante;
}

/**
 * @brief Convierte un entero a flotante y le suma uno usando C puro.
 *
 * @param numero_entero Valor entero que se convertirá a float.
 * @return Resultado de la conversión a float más uno.
 */
float to_float(int numero_entero){
    float numero_flotante = (float) numero_entero;  
    numero_flotante = numero_flotante + 1;
    return numero_flotante;
}

/**
 * @brief Método expuesto a Python que convierte un entero a float mediante ensamblador.
 *
 * Recibe un único argumento entero desde Python, lo convierte a float
 * sumándole diez y retorna un objeto PyFloat.
 *
 * @param self   Referencia al módulo (no usado).
 * @param args   Tupla con los argumentos pasados desde Python.
 * @return PyObject* apuntando al objecto py de tipo float o NULL con excepción.
 */
static PyObject* int_to_float_asm(PyObject* self, PyObject* args){
    int numero_entero;
    // Extrae un entero de la tupla de argumentos
    if (!PyArg_ParseTuple(args, "i", &numero_entero)) {
        return NULL; // Error: argumento no válido
    }

    float resultado = to_float_asm(numero_entero);

    // Se crea un nuevo objeto PyFloat
    PyObject *py_float = PyFloat_FromDouble((double)resultado);
    if (!py_float) {
        return PyErr_NoMemory();
    }

    return py_float;
}


/**
 * @brief Método expuesto a Python que convierte un entero a float en C puro.
 *
 * Recibe un entero desde Python, lo convierte a float sumándole uno
 * y retorna un objeto PyFloat.
 *
 * @param self   Referencia al módulo (no usado).
 * @param args   Tupla con los argumentos pasados desde Python.
 * @return PyObject*  apuntando al objecto py de tipo float o NULL con excepción.
 */
static PyObject* int_to_float(PyObject* self, PyObject* args) {
    int numero_entero;
    // Extrae un entero de la tupla de argumentos
    if (!PyArg_ParseTuple(args, "i", &numero_entero)) {
        return NULL; // Error: argumento no válido
    }

    float resultado = to_float(numero_entero);

    // Utiliza PyObject_New para crear el objeto PyFloat
    PyFloatObject *py_float = (PyFloatObject *)PyObject_New(PyFloatObject, &PyFloat_Type);
    if (!py_float) {
        return PyErr_NoMemory();
    }
    // Asignar el valor flotante
    py_float->ob_fval = resultado;

    return (PyObject *)py_float;
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
static PyMethodDef convert_int_to_float_Methods[] =
{ 
     {"convertToFloatAsm", int_to_float_asm, METH_VARARGS, "Devuelve un dato de tipo float a partir de un entero"},
     {"convertToFloat", int_to_float, METH_VARARGS, "Devuelve un dato de tipo float a partir de un entero"},
     {NULL, NULL, 0, NULL} /* Marca el final de la lista */
};

/**
 * @brief Estructura de definición del módulo.
 */
static struct PyModuleDef convertionmod =
{
     PyModuleDef_HEAD_INIT,
     "convert_int_to_float", /* Nombre del módulo */
     "convertir enteros a flotante",  /* Documentación del módulo */         
     -1,                         /* Tamaño del estado (módulos sin estado usan -1) */
     convert_int_to_float_Methods  /* Tabla de métodos */
};

/**
 * @brief Punto de inicialización del módulo.
 *
 * Llamado al importar el módulo en Python.
 */
PyMODINIT_FUNC PyInit_convert_int_to_float(void)
{
    return PyModule_Create(&convertionmod);
}




