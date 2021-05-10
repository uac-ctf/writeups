# A Bowl of Pythons

The challenge provided a small python script which requested a flag.
The script would assemble the flag from internally stored values and then compare the result with the provided input.

``` $ python3 chal.py
Welcome to SDCTF's the first Reverse Engineering challenge.
Input the correct flag: test
Incorrect flag! You need to hack deeper...
```

A simple way of solving it was to do the calculations, and print the result.
This can be achieved by placing the following code in the top of function ```e()```. The code is taken from the script it self.
Actually, this code could be almost anywhere on the file...

```
    start=b('{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])))
    end = '}'
    middle=bytes((f[i] ^ (a(i) & 0xff)) for i in range(len(f)))
    print(start+middle.decode()+end)
    return
```

The result would be the following:

```
$ python3 solve.py
sdctf{v3ry-t4sty-sph4g3tt1}
```

