# Variables
SRC_DIR     := src/c_src
BUILD_DIR   := build
PY_LIB_NAME := convert_int_to_float
PY_SCRIPT   := api_request.py

C_FILE          := $(SRC_DIR)/convertion.c
ASM_FILE        := $(SRC_DIR)/adder.asm
ASM_OBJ_FILE    := $(BUILD_DIR)/adder.o
C_OBJ_FILE		:= $(BUILD_DIR)/convertion_ctypes.o

# Reglas
all:
	@mkdir -p $(BUILD_DIR)
	nasm -f elf64 $(ASM_FILE) -o $(ASM_OBJ_FILE)
	gcc -fPIC -c $(C_FILE) -o $(C_OBJ_FILE)
	gcc -shared -W -o $(BUILD_DIR)/lib_convertion_ctypes.so $(C_OBJ_FILE)
	python3 setup.py sdist bdist_wheel

install: all
	pip install . --upgrade

gdb:
	chmod +x run_gdb.sh
	./run_gdb.sh 

clean:
	sudo rm -rf $(BUILD_DIR) *.egg-info __pycache__ dist


.PHONY: all install clean
