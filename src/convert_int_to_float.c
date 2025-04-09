#include <Python.h>

extern int adder(int a, int b);

float _int_to_float(int numero_entero){
    float numero_flotante = (float) numero_entero;  //Convertir a flotante
    int a = 5, b = 3, result;
    result = adder(a,b);    
    numero_flotante = numero_flotante + result;
    printf("Flotante version 3.1: %.2f\n", numero_flotante);

    return numero_flotante;
}


static PyObject* int_to_float(PyObject* self, PyObject* args){
    int numero_entero;
    if (!PyArg_ParseTuple(args, "i", &numero_entero))
        return NULL;
    float _float = _int_to_float(numero_entero);
    PyFloatObject *numero_flotante = (PyFloatObject *)PyObject_Malloc(sizeof(PyFloatObject));

    if (numero_flotante == NULL)
        return PyErr_NoMemory();
    
    if (PyObject_Init((PyObject *)numero_flotante, &PyFloat_Type) == NULL) {
        PyObject_Free(numero_flotante);  // Free the memory if initialization fails.
        return NULL;
    }

    numero_flotante->ob_fval = _float;
    return (PyObject *)numero_flotante;
}

static PyObject* version(PyObject* self)
{
    return Py_BuildValue("s","Version 0.01");
}

static PyMethodDef convert_int_to_float_Methods[] =
{
     {"convertToFloat", int_to_float, METH_VARARGS, "Devuelve un dato de tipo float a partir de un entero"},
     {"version", (PyCFunction)version, METH_VARARGS, "Devuelve la version del modulo"},
     {NULL, NULL, 0, NULL}
};


static struct PyModuleDef convertionmod =
{
     PyModuleDef_HEAD_INIT,
     "convert_int_to_float", 
     "convertir enteros a float",          
     -1,          
     convert_int_to_float_Methods
};
 
  // Inicializacion del modulo
PyMODINIT_FUNC PyInit_convert_int_to_float(void)
{
    return PyModule_Create(&convertionmod);
}




