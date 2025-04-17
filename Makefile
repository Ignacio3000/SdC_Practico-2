# Variables
SRC_DIR     := src
BUILD_DIR   := build
PY_LIB_NAME := convert_int_to_float

C_FILE      := $(SRC_DIR)/$(PY_LIB_NAME).c
ASM_FILE    := $(SRC_DIR)/adder.asm
OBJ_FILE    := $(BUILD_DIR)/adder.o

# Reglas
all:
	@mkdir -p $(BUILD_DIR)
	nasm -f elf64 $(ASM_FILE) -o $(OBJ_FILE)
	python3 setup.py sdist bdist_wheel

install: all
	pip install . --upgrade

clean:
	sudo rm -rf $(BUILD_DIR) *.egg-info __pycache__ dist


.PHONY: all install clean
