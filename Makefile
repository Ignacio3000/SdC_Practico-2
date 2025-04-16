# Variables
SRC_DIR     := src
BUILD_DIR   := build
PY_LIB_NAME := convert_int_to_float

SO_NAME     := $(BUILD_DIR)/$(PY_LIB_NAME).$(shell python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))").so
C_FILE      := $(SRC_DIR)/$(PY_LIB_NAME).c
ASM_FILE    := $(SRC_DIR)/adder.asm
OBJ_FILE    := $(BUILD_DIR)/adder.o

CFLAGS  := -m64 -shared -fPIC -g 
LDFLAGS := $(shell python3-config --cflags --ldflags)

# Reglas
all:
	@mkdir -p $(BUILD_DIR)
	nasm -f elf64 $(ASM_FILE) -o $(OBJ_FILE)
	gcc $(CFLAGS) -o $(SO_NAME) $(C_FILE) $(OBJ_FILE) $(LDFLAGS)

install: all
	sudo python3 setup.py install

clean:
	sudo rm -rf $(BUILD_DIR) *.egg-info __pycache__ dist

.PHONY: all install clean
