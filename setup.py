from setuptools import setup, Extension

convert_int_to_float = Extension(
    'convert_int_to_float',
    sources=['src/convert_int_to_float.c'],
    extra_objects=['build/adder.o'],
    extra_compile_args=['-g', '-O0', '-fPIC'], 
    extra_link_args=[]                           
)

setup(
    name='convert_int_to_float',
    version='0.1.0',
    ext_modules=[convert_int_to_float],
)
