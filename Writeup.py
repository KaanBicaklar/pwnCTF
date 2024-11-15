from pwn import *
from randcrack import RandCrack

rc = RandCrack()

t = remote('HOST', 1337)



i=0
while not rc.state:
    i +=1
    t.recvuntil(b'> ')
    t.sendline(b'12345678')
    val = t.recvuntil(b'\n')
    print( i," alinan : ",val.split(b'\n')[0])
    num = int(val.split(b'\n')[0])
    rc.submit(num)
print ("cikti")
guess = rc.predict_getrandbits(32)
print ("gonderilen : ",guess)
t.sendline(str(guess))
t.interactive()


