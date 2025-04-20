from setuptools import setup, Extension

convert_to_int_asm = Extension(
    'float_to_int_asm',
    sources=['src/c_src/convert_float_to_int.c'],
    extra_objects=['build/convert_to_int.o'],
    extra_compile_args=['-g', '-O0', '-fPIC'], 
    extra_link_args=[]                           
)

conversion_float_to_int = Extension(
    'float_to_int_c',
    sources=['src/c_src/wrapper.c', 'src/c_src/convertion.c'],
    extra_compile_args=['-g', '-O3', '-fPIC'],
)


setup(
    name='my_wrappers',       
    version='0.1.0',
    description='Dos wrappers C para Python',
    ext_modules=[
        convert_to_int_asm,
        conversion_float_to_int,
    ],
)