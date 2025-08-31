; 2_2_seminar.asm 
section .data
message:       db  'hello, world!', 0
error_message: db  'hello, errors!', 0

section .text
global _start

exit:
    mov  rax, 60
    xor  rdi, rdi          
    syscall

string_length:
    xor rax, rax
.loop:
    cmp byte [rdi+rax], 0
    je .end
    inc rax
    jmp .loop
.end:
    ret

print_string:
    push rdi              ; Сохраняем rdi перед вызовом string_length
    call string_length    ; Получаем длину строки в rax
    pop  rsi              ; Восстанавливаем rdi и одновременно перемещаем его в rsi
    mov  rdx, rax         ; Длина строки
    mov  rax, 1
    mov  rdi, 1
    syscall
    ret

_start:
    mov  rdi, message  
    call print_string
    call exit

