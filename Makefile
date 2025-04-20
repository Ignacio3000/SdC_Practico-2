# Variables
SRC_DIR     := src/c_src
BUILD_DIR   := build
PY_LIB_NAME := convert_int_to_float
PY_SCRIPT   := api_request.py

C_FILE          := $(SRC_DIR)/convertion.c
ASM_FILE        := $(SRC_DIR)/convert_to_int.asm
ASM_OBJ_FILE    := $(BUILD_DIR)/convert_to_int.o
C_OBJ_FILE		:= $(BUILD_DIR)/convertion_ctypes.o

# Reglas
all:
	@mkdir -p $(BUILD_DIR)
	nasm -f elf64 $(ASM_FILE) -o $(ASM_OBJ_FILE)
	gcc -fPIC -c $(C_FILE) -o $(C_OBJ_FILE)
	gcc -shared -W -o $(BUILD_DIR)/lib_convertion_ctypes.so $(C_OBJ_FILE)
	python3 setup.py sdist bdist_wheel

install: 
	pip install . --upgrade

gdb:
	gdb -q --args  python3-dbg src/scripts/api_c_asm.py

benchmark:
	PYTHONPATH=. python3 -m perfomance_tests.benchmark
	
compare:
	pyperf compare_to --table  python_converter.json ctypes_converter.json asm_converter.json

clean:
	sudo rm -rf $(BUILD_DIR) *.egg-info __pycache__ dist
	rm  -f ctypes_converter.json asm_converter.json python_converter.json


.PHONY: all install clean

