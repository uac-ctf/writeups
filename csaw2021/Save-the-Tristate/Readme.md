# Challenge Description

So it was just another day in Danville when Phineas and Ferb were making a new device to communicate with Meep as he travels across the galaxy. To make a device suitable for galatic communication and secure enough to be safe from alien hackers, they decide to protect their device with QKD! Unfortunately, due to Phineas & Co singing their usual musical numbers about their inventions, Doofenshmirtz has caught wind of this technology and wants to use it to take over the Tristate area, using his brand new Qubit-Disrupt-inator. Naturally I, Major Monogram, have to send you, Perry the Platypus, on a mission to stop Doofenshmirtz from disrupting Phineas and Ferb's qubits with his diabolical inator. So grab your tiny fedora and doo-bee-doo-bee-doo-ba-doo your way over to stop Doofenshmirtz! Mission:

    Receive # of qubits that translate to the flag
    Measure qubits in your own basis
    Monogram tells you how many qubits were measured correctly, but not which ones
    Go back and fix it
    Get it right

---
## Intro

QKD (Quantum Key Distribution) is a technology that uses quantum mechanics to allow two parties (like Phineas & Ferb) to create a shared, secret key for secure communication, with the BB84 protocol being a prime example of how this is done. The provided solution script solves the CTF challenge by systematically figuring out the correct quantum measurement bases for a series of qubits, using feedback from "Major Monogram" (the server) to correct any wrong guesses, and then translating the measured qubit states into the final flag.


## Quantum Key Distribution (QKD)

**QKD** is a secure communication method that uses the principles of quantum mechanics to establish a shared secret key between two parties (Alice and Bob - or in this case, Phineas & Ferb). This key can then be used with traditional encryption algorithms to secure their messages.

The core idea is that observing a quantum system generally disturbs it. This means if an eavesdropper (like Doofenshmirtz with his Qubit-Disrupt-inator) tries to intercept and measure the qubits being exchanged, they will inevitably introduce detectable anomalies. Alice and Bob can then check for these disturbances. If significant disturbances are found, they discard the key and try again. If not, they can be confident that the key is secret.

In essence, QKD provides a way to detect eavesdropping as it happens, rather than relying on the computational difficulty of breaking an encryption algorithm after the fact.

## The BB84 Protocol (Bennett & Brassard 1984)

The BB84 protocol is one of the first and most well-known QKD protocols. Here's how it typically works:

1.  Alice prepares and Sends Qubits:
    * Alice wants to send a string of random bits to Bob.
    * For each bit, she randomly chooses one of two bases to encode it:
        * Rectilinear basis (+): Encodes bit '0' as a qubit in state $|0\rangle$ and bit '1' as a qubit in state $|1\rangle$.
        * Diagonal basis (x): Encodes bit '0' as a qubit in state $|+\rangle$ and bit '1' as a qubit in state $|-\rangle$.
    * She sends the stream of prepared qubits to Bob over a quantum channel.

2.  Bob measures Qubits:
    * For each qubit Bob receives, he randomly chooses one of the two bases (+ or x) to measure it in. He doesn't know Alice's basis choices.
    * If Bob chooses the same basis as Alice used for encoding: He gets the correct bit value with 100% certainty.
    * If Bob chooses a different basis: He gets a random bit (50% chance of being '0', 50% chance of being '1'), regardless of Alice's original bit.

3.  Basis Reconciliation (Sifting) - The Public Discussion (Monogram's Intel):
    * After all qubits are sent and measured, Bob communicates with Alice over a public (but not necessarily secure) classical channel.
    * They compare the bases they used for each qubit. They do not reveal the bit values they measured or sent.
    * They discard all the bits where their bases didn't match. The remaining bits form the "sifted key." On average, this will be about 50% of the originally sent bits.

4.  Error Estimation and Correction:
    * Alice and Bob publicly compare a small random subset of their sifted key bits.
    * If there are discrepancies beyond what's expected from noise, they assume an eavesdropper (Doofenshmirtz!) was present and abort the protocol.
    * If the error rate is low enough, they use error correction protocols to remove errors and privacy amplification techniques to distill a shorter, highly secure final key.

## The CTF Challenge & Attack Strategy

The CTF challenge cleverly twists the BB84 scenario. Instead of comparing bases directly, "Major Monogram" (the server) gives you feedback on how many qubits you measured correctly. The attack uses this feedback as an oracle to deduce Phineas and Ferb's (the server's) bases one by one.

Let's look at your script's logic:

1.  Connection:
    `conn = remote('misc.chal.csaw.io', 5001)`
    This connects to Phineas and Ferb's device (the server).

2.  Iterative Basis Guessing:
    * The attack attempts to determine the correct basis for each of the 256 qubits sequentially.
    * `bases = ['x']`: It starts by assuming the first qubit was encoded in the 'x' (diagonal) basis.
    * In the main `while` loop, it keeps adding 'x' as the guess for the next qubit: `bases.append('x')`.
    * It then sends its current sequence of guessed bases (e.g., "x", then "xx", then "xx+", etc.) to the server:
        `conn.sendline(bytes(''.join(bases), encoding='utf-8'))`

3.  Monogram's Feedback (The Oracle):
    * `r = conn.recvline()`: It receives feedback from the server.
    * The crucial line:
        `if '0' != r.decode('utf-8').split(' ')[1].replace("\r\n",""):`
        This checks the server's response. It seems the server responds with a message where '0' (as the second word) indicates that all bases sent so far are correct.
        * If the server's response indicates an error (i.e., the relevant part is not '0'), it means the last basis added was incorrect.
        * The script then "fixes" it by changing the last guessed basis from 'x' to '+':
            `bases[-1] = '+'`
    * If the server's response indicates '0' (no errors for the current set of bases), it means the last basis ('x') was correct, and the script proceeds to guess 'x' for the next qubit.

4.  Receiving and Decoding Qubits (Final Stage):
    * When `len(bases) == 256 + 1` (meaning all 256 bases are determined, accounting for an extra append that's later popped), the script is ready to decode.
    * `qbs = r.decode('utf-8').split('\r\n')`: It gets the list of qubit states (represented as complex numbers like '1.0 + 0.0i') from the server.
    * The script iterates through its determined `bases` and the received `qbs` to reconstruct the binary key:
        * If `bases[i] == '+'` (Rectilinear/Z-basis):
            * `'1.0 + 0.0i'` (representing $|0\rangle$) is decoded as bit '0'.
            * `'0.0 + 1.0i'` (representing $|1\rangle$) is decoded as bit '1'.
        * If `bases[i] == 'x'` (Diagonal/X-basis):
            * `'0.707 + 0.707i'` (proportional to $|+\rangle$) is decoded as bit '0'.
            * `'-0.707 + 0.707i'` (proportional to $|-\rangle$) is decoded as bit '1'.

    * `key = binascii.unhexlify('%x' % int(''.join(bits), 2))`: This converts the decoded bits binary  string into its ASCII/byte representation! (Thanks `Rackham`!)

In summary, the attack isn't performing standard BB84 basis reconciliation. Instead, it's exploiting a monogram's feedback that effectively tells it if its latest basis choice, combined with previously confirmed correct ones, introduces an error. This allows it to determine each basis iteratively. If a choice is wrong, it flips it, knowing the new choice must be right (as there are only two options).

With this approach, both me and `Rackham` were able to retrieve the flag and stop Doofenshmirtz's diabolical plans!

```
flag{MO0O0O0O0M PH1NE4S & F3RB R T4LK1NG 2 AL1ENS 0V3R QKD!!!}
```

---
## PoC
```
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
```
Thanks!
mluis

