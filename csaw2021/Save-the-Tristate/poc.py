#!/usr/bin/python3
import sys
from pwn import *
import binascii

conn = remote('misc.chal.csaw.io', 5001)

bases = ['x']

while True:
    if len(bases) == 256 + 1:
        bits = []
        r = conn.recvuntil(b'What is the key?: \r\n')
        print(r)
        qbs = r.decode('utf-8').split('\r\n')
        qbs.pop()
        qbs.pop()
        bases.pop()
        for i in range(len(bases)):
            if bases[i] == '+':
                if qbs[i] == '0.0 + 1.0i':
                    bits.append('1')
                elif qbs[i] == '1.0 + 0.0i':
                    bits.append('0')
            elif bases[i] == 'x':
                if qbs[i] == '-0.707 + 0.707i':
                    bits.append('1')
                elif qbs[i] == '0.707 + 0.707i':
                    bits.append('0')
            else:
                print(bases[i], qbs[i])
        key = binascii.unhexlify('%x' % int(''.join(bits), 2))
        print(key)
        conn.sendline(key)
        r = conn.recvline()
        print(r)
        conn.interactive()
        
    r = conn.recvline()
    print(r)
    print(len(bases))
    conn.sendline(bytes(str(len(bases)), 'utf-8'))
    r = conn.recvline()
    print(r)
    print(''.join(bases))
    conn.sendline(bytes(''.join(bases), encoding='utf-8'))
    r = conn.recvline()
    print(r)
    if '0' != r.decode('utf-8').split(' ')[1].replace("\r\n",""):
        # error
        bases[-1] = '+'
    else:
        # no error
        bases.append('x')
