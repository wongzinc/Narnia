BITS 32
    jmp short one 

two: 
; ssize_t write(int fd, const void *buf, size_t count);
    pop ecx ; 
    xor eax, eax
    mov al, 4
    xor ebx, ebx
    inc ebx
    xor edx, edx
    mov dl, 15
    int 0x80

; void _exit(int status)
    mov al, 1 ; exit syscall 1
    dec ebx  ; status=0
    int 0x80

one: 
    call two 
    db "Hello, world",0x0a,0x0d