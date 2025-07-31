.intel_syntax noprefix
.global _start

_start:
    mov rdi, [rsp] # argc
    lea rsi, [rsp + 8] # argv
    call main

    # sys_exit, rax = main exit code
    mov rdi, rax
    mov rax, 60
    syscall