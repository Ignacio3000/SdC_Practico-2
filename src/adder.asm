[BITS 64]

section .text
global adder

adder:
    ; Argumentos en 64 bits:
    ; RDI -> primer argumento
    ; RSI -> segundo argumento
    ; El resultado se retorna en RAX
    mov rax, rdi
    add rax, rsi
    ret