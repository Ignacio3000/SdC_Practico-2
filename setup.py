from setuptools import setup, Extension

convert_int_to_float = Extension(
    'convert_int_to_float',
    sources=['src/convert_int_to_float.c'],
    extra_objects=['build/adder.o'],
    extra_compile_args=['-g', '-O0', '-fPIC'], 
    extra_link_args=[]                           
)

conversion_float_to_int = Extension(
    'float_to_int_c',
    sources=['src/c_src/wrapper.c', 'src/c_src/convertion.c'],
    extra_compile_args=['-g', '-O3', '-fPIC'],
)


setup(
    name='convert_int_to_float',
    version='0.1.0',
    ext_modules=[convert_int_to_float],
)