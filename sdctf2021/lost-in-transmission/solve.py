
f = open('flag.dat', 'rb')
data = f.read()

for c in data:
    print(chr(c >> 1), end='')
