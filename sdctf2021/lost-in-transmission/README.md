# Lost in Transmission

The challenged provided a binary file without any structure.
Analysing the content with xxd:
```
xxd flag.dat
00000000: e6c8 c6e8 ccf6 ae60 dc88 66e4 ccaa 98be  .......`..f.....
00000010: dab2 be8e 6060 c8be e662 a4fa            ....``...b..
```

The file is named flag, so thats a strong hint. It has the size of a typical flag, and the content is composed by bytes in the high side.
We assumed that some bit as lost in the transmission and we add to add that bit somewhere, probably at the start, and then shift the all values.
However, that was not the case... we simply needed to shift all bytes by one bit.

the solving script:
```
f = open('flag.dat', 'rb')
data = f.read()

for c in data:
    print(chr(c >> 1), end='')
```

the solution:
```
$ python3 solve.py
sdctf{W0nD3rfUL_mY_G00d_s1R}
```
