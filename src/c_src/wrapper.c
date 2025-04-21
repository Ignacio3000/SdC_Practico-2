// wrapper.c
#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Declaración de las funciones originales
int convert_and_add_one_time(float x);
int convert_and_add_one_million(float x);

// Envoltura para convert_and_add_one_time para que python pueda llamarla
static PyObject* py_convert_and_add_one_time(PyObject* self, PyObject* args) {
    float x;
    if (!PyArg_ParseTuple(args, "f", &x)) //convierte un argumento de Python (float) a un float de C.
        return NULL;

    int result = convert_and_add_one_time(x); //llamamos a la funcion 
    return PyLong_FromLong(result); //convierte el resultado de C (entero) a un int de Python.
}

// Envoltura para convert_and_add_one_million para que python pueda llamarla
static PyObject* py_convert_and_add_one_million(PyObject* self, PyObject* args) { 
    float x;
    if (!PyArg_ParseTuple(args, "f", &x)) //convierte un argumento de Python (float) a un float de C.
        return NULL;

    int result = convert_and_add_one_million(x); //llamamos a la funcion 
    return PyLong_FromLong(result); //convierte el resultado de C (entero) a un int de Python.
}

// Lista de métodos expuestos le dice a Python qué funciones exporta el módulo, con sus nombres y descripciones.
static PyMethodDef float_to_int_c_Methods[] = {
    {"convert_and_add_one_time", py_convert_and_add_one_time, METH_VARARGS, "Convierte y suma una vez"},
    {"convert_and_add_one_million", py_convert_and_add_one_million, METH_VARARGS, "Convierte y suma un millón de veces"},
    {NULL, NULL, 0, NULL}
};

// Definición del módulo función especial que se llama cuando se hace import convertion_float_to_int desde Python.
static struct PyModuleDef convertion_float_to_int_definition = {
    PyModuleDef_HEAD_INIT,
    "convertion_float_to_int",
    "Módulo que envuelve funciones en C para sumar enteros",
    -1,
    float_to_int_c_Methods
};

// Inicializador del módulo
PyMODINIT_FUNC PyInit_float_to_int_c(void) {
    return PyModule_Create(&convertion_float_to_int_definition);
}
