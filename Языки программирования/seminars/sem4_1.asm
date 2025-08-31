%define O_RDONLY 0 
%define PROT_READ 0x1
%define MAP_PRIVATE 0x2
%define SYS_WRITE 1
%define SYS_OPEN 2
%define SYS_MMAP 9
%define FD_STDOUT 1
%define SYS_FSTAT 5


section .data
    fname: db 'hello.txt', 0

section .bss
    file_size resq 1

section .text
global _start

; exit system call to shut down correctly
exit:
    mov  rax, 60
    xor  rdi, rdi
    syscall

; print_string function (prints null-terminated string)
print_string:
    push rdi
    call string_length
    pop  rsi
    mov  rdx, rax 
    mov  rax, SYS_WRITE
    mov  rdi, FD_STDOUT
    syscall
    ret

; string_length function
string_length:
    xor  rax, rax
.loop:
    cmp  byte [rdi+rax], 0
    je   .end 
    inc  rax
    jmp .loop 
.end:
    ret

; print_substring function
print_substring:
    mov  rdx, rsi 
    mov  rsi, rdi
    mov  rax, SYS_WRITE
    mov  rdi, FD_STDOUT
    syscall
    ret

_start:
    ; Open the file
    mov  rax, SYS_OPEN
    mov  rdi, fname
    mov  rsi, O_RDONLY
    syscall
    test rax, rax  ; Check for errors
    js exit        ; Negative return values are errors

    mov  rbx, rax

    ; Get file size using fstat
    mov  rax, SYS_FSTAT
    mov  rdi, rbx          ; file descriptor
    lea  rsi, [rsp-128]    ; address of struct stat on the stack
    syscall
    test rax, rax
    js exit

    mov rdx, [rsi + 48]    ; get file size from struct stat
    mov [file_size], rdx


    ; Map the file into memory
    mov  rax, SYS_MMAP
    xor  rdi, rdi
    mov  rsi, rdx
    mov  r10d, MAP_PRIVATE
    mov  r8d, PROT_READ
    mov  r9, rbx
    xor  rdx, rdx
    syscall
    test rax, rax
    js exit

    mov rdi, rax
    mov rsi, [file_size]
    call print_substring

    ; Unmap the memory
    mov rax, 11
    mov rsi, rdi
    mov rdi, rsi
    syscall
    test rax, rax
    js exit

    ; Close the file
    mov rax, 3
    mov rdi, rbx
    syscall
    test rax, rax
    js exit

    call exit

