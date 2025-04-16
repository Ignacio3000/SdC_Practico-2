from distutils.core import setup, Extension

convert_int_to_float_module = Extension(
    'convert_int_to_float',
    sources=['src/convert_int_to_float.c'],
    extra_objects=['build/adder.o']
)

setup(ext_modules=[convert_int_to_float_module])