global to_int_asm
global to_int_asm_mil

section .text

; float en XMM0 → int en EAX + 1
to_int_asm:
    ; Convertir de float (xmm0) a int (eax), redondeando
    cvtss2si eax, xmm0

    ; Sumar 1
    add eax, 1

    ; Retornar (valor en eax)
    ret


to_int_asm_mil:
    ; Convertir de float (xmm0) a int (eax), redondeando
    cvtss2si eax, xmm0

    ; Inicializar contador en ecx con 1000
    mov ecx, 1000

suma_loop:
    add eax, 1        ; Sumar 1
    loop suma_loop    ; Decrementa ecx y salta si no es cero

    ; Retornar (valor en eax)
    ret



