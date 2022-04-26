from pwn import *
import itertools

def anda(key, n):
    for _ in itertools.repeat(None, n):
        p.sendline(key)

p = remote("35.184.230.50",3000)
# p = process('game.bak')
string = "epic_dijkstra.4441990"
nome = bytes(string, 'ascii')

p.sendline(nome)
p.sendline(b"2910000-3076-5273-1")

anda(b'w', 2)
anda(b'a', 2)
anda(b'w', 9)
anda(b'd', 1)
anda(b'w', 4)
anda(b's', 4)
anda(b'a', 1)
anda(b's', 6)
anda(b'a', 3)
anda(b's', 1)
anda(b'a', 6)
anda(b's', 1)
anda(b'a', 3)
anda(b'd', 3)
anda(b'w', 3)
anda(b'a', 1)
anda(b'w', 2)
anda(b'a', 5)
anda(b'w', 1)
anda(b'a', 1)
anda(b'd', 1)
anda(b'w', 6)
anda(b'a', 1)
anda(b'w', 1)
anda(b'a', 1)
anda(b'w', 5)
anda(b'a', 2)
anda(b'w', 2)

p.sendline(b'a')
p.sendline(b'a')
p.sendline(b'a')
p.sendline(b'a')
p.sendline(b'a')

for i in range(1000):
    try:
        print(p.recvline())
    except:
        pass