from distutils.core import setup, Extension

# Definimos el modulo de extension
convert_int_to_float_module = Extension('convert_int_to_float', sources=['convert_int_to_float.c'], extra_objects=['adder.o'])

# Ejecutar el setup
setup(ext_modules=[convert_int_to_float_module])