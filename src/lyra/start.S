.globl _start
.type _start, @function
_start:
    # Call main (no arguments)
    call main

    # Exit syscall with return value from main
    mov %rax, %rdi      # move return value into exit code
    mov $60, %rax       # syscall number for exit
    syscall