from setuptools import setup, Extension

convert_to_int = Extension(
    'convert_to_int',
    sources=['src/convert_float_to_int.c'],
    extra_objects=['build/convert_to_int.o'],
    extra_compile_args=['-g', '-O0', '-fPIC'], 
    extra_link_args=[]                           
)

setup(
    name='convert_to_int',
    version='0.1.0',
    ext_modules=[convert_to_int],
)
