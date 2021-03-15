# NahamCon2021
# DDR, medium 497pts

from PIL import Image

im = Image.open("ddr.png")

sq_size = 64
sq_x = im.width // sq_size
sq_y = im.height // sq_size

path = 'rruuulurrrdrrruluuldluulddluulllddr'
start = (10, 7)

res = [['' for x in range(sq_x)] for y in range(sq_y)] 
for y in range(0, sq_y):
    for x in range(0, sq_x):
        res[y][x] = "{:s}".format(chr(im.getpixel((x * sq_size + 1, y * sq_size + 1))[0]))

x = 10
y = 7
print('f', end='')
for c in path:
    if c == 'r':
        x += 1
    elif c == 'l':
        x -= 1
    elif c == 'u':
        y -= 1
    elif c == 'd':
        y += 1

    print(res[y][x], end='')

print()
