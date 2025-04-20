[BITS 64]

section .text

global to_int_asm
global to_int_asm_mil

section .text

; float en XMM0 → int en RAX + 1
to_int_asm:
    ; Convertir de float (xmm0) a int (rax), redondeando

    cvtss2si rax, xmm0

    ; Sumar 1
    add rax, 1

    ; Retornar (valor en rax)
    ret


to_int_asm_mil:
    ; Convertir de float (xmm0) a int (eax), redondeando
    cvtss2si rax, xmm0

    ; Inicializar contador en ecx con 1000
    mov rcx, 1000000

suma_loop:
    cvtss2si rax, xmm0 ; Sumar 1
    add rax, 1        
    loop suma_loop    ; Decrementa rcx y salta si no es cero

    ; Retornar (valor en eax)
    ret