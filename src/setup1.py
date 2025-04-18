from setuptools import setup, Extension

convertion_float_to_int = Extension(
    'convertion_float_to_int',
    sources=['src/wrapper.c' , 'src/convertion.c'],
    extra_compile_args=['-g', '-O3', '-fPIC'], 
    extra_link_args=[]                           
)

setup(
    name='convert_int_to_float',
    version='0.1.0',
    ext_modules=[convertion_float_to_int],
)
