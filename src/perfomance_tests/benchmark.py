import pyperf
import convert_int_to_float
import random

from scripts import api_only_python
from scripts import api_request

def bench_asm():
    api_request.main()

def bench_python():
    api_only_python.main()

if __name__ == "__main__":
    runner = pyperf.Runner()
    # inner_loops repite N veces cada función antes de medir
    runner.bench_func('ASM converter', bench_asm, inner_loops=100)
    runner.bench_func('Pure-Python converter', bench_python, inner_loops=100)
    
#runner = pyperf.Runner()
#runner.bench_func('Python + C + ASM', api_only_python.main,inner_loops=100)
#runner.bench_func('Only python', api_request.main,inner_loops=100)