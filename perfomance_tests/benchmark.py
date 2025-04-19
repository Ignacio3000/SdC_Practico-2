import os
import pyperf
import convert_int_to_float
import random

from src.scripts import api_only_python, api_ctypes, api_c_asm

PY_BENCH      = False
CTYPES_BENCH  = False
ASM_BENCH     = True


def bench_asm():
    #api_c_asm.main()
    api_c_asm.convert_and_add(1)

def bench_python():
    #api_only_python.main()
    api_only_python.convert_and_add(1)

def bench_ctypes():
    #api_ctypes.main()
    api_ctypes.convert_and_add(1)


runner = pyperf.Runner()

# Ejecutamos los tres benchs
if ASM_BENCH:
    asm_bench     = runner.bench_func('converter', bench_asm,    inner_loops=100)
else:
    asm_bench     = None

if CTYPES_BENCH:
    ctypes_bench  = runner.bench_func('converter', bench_ctypes, inner_loops=100)
else:
    ctypes_bench  = None

if PY_BENCH:
    python_bench = runner.bench_func('converter',  bench_python, inner_loops=100)
else:
    python_bench  = None
    

# Sólo si bench_func() devolvió un Benchmark real, creamos el JSON
for bench, fname in [
    (asm_bench,    'asm_converter.json'   ),
    (ctypes_bench, 'ctypes_converter.json'),
    (python_bench, 'python_converter.json'),
]:
    if bench is not None:
        bench.dump(fname, compact=True, replace=True)


