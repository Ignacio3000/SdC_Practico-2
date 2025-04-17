[BITS 64]

section .text
global adder
global convert_to_float

adder:
    ; RDI -> primer argumento
    ; RSI -> segundo argumento
    ; El resultado se retorna en XMM0
    
    sub   rsp, 16           ; reservar 16 bytes para el guardar los argumentos
    mov   [rsp], rdi
    mov   [rsp+8], rsi
    fild  dword [rsp]       ; carga el entero desde el stack al FPU
    fild  dword [rsp+8]     ; carga el entero desde el stack al FPU
    fadd  st1
    fstp  dword [rsp]       ; almacena el  resultado de la suma en el stack
    movss xmm0, dword [rsp] ; mueve el valor de doble precisión a xmm0
    add   rsp, 16           ; libera el espacio reservado en el stack
    ret                     ; el resultado se retorna en xmm0

convert_to_float:
    sub   rsp,   8              ; reservar 8 bytes para el guardar el entero
    mov   [rsp], rdi            ; mueve el entero de rdi a esa posición en el stack
    movss xmm0, dword [rsp]     ; mueve el valor de doble precisión a xmm0
    add   rsp, 8                ; libera el espacio reservado en el stack
    ret                         ; el resultado se retorna en xmm0
