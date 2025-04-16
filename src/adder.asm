[BITS 64]

section .text
global adder
global convert_to_float

adder:
    ; RDI -> primer argumento
    ; RSI -> segundo argumento
    ; El resultado se retorna en RAX
    mov rax, rdi
    add rax, rsi
    ret

convert_to_float:
    sub   rsp,   8              ; reservar 8 bytes para el guardar el entero
    mov   [rsp], rdi            ; mueve el entero de rdi a esa posición en el stack
    fild  dword [rsp]           ; carga el entero desde el stack al FPU
    fstp  dword [rsp]           ; almacena el valor convertido en la misma posición (o en otra, según se requiera)
    movss xmm0, dword [rsp]     ; mueve el valor de doble precisión a xmm0
    add   rsp, 8                ; libera el espacio reservado en el stack
    ret
