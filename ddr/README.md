
# DDR

It's Dance Dance Revolution! You already know how to play!


## Solve

The challenge presents a message related to the famous [DDR](https://en.wikipedia.org/wiki/Dance_Dance_Revolution) game and then an image with several squares and arrows with collors. 
The arrows are similar to the ones from the game.

![ddr](https://github.com/uac-ctf/nahamcon2021/raw/main/ddr/ddr.png)

In most squares the background is gray, while the center square is red. We assumed that the red square would be the start of something.
Then we noticed that the squares had small variations in their color.

In RGB, gray color is composed by 3 channel with the same value. E.g. (42, 42, 42).

We then made a script to convert the first channel to an ASCII representation, and we got the following output:


```
8 e 1 3 0 d b 4 2 9 1 c 4 f 2 9 0 0 2 2 5
e f b f a 2 5 7 2 2 5 b e 2 b 3 c 9 e 1 3
7 0 6 b 3 c 1 a 4 e } 2 f 7 9 2 9 b 6 c 6
b c 8 3 d e 8 c 7 d c 4 c 6 9 0 4 8 a 1 d
8 c f d a 5 8 b 8 c 2 a 2 7 0 6 7 5 c 5 4
c 7 4 c 9 a 5 4 6 7 b 7 { 6 a b 4 f e 0 0
8 d d 2 4 7 b f 3 4 8 5 g f 5 c 4 7 e f d
e d f 2 e 2 6 d f c ÿ l a 2 0 0 7 0 1 e 9
4 5 2 2 0 b b a 3 f 0 c b 1 3 4 3 2 c 2 e
4 4 d 6 5 7 d 1 e b 9 6 a f 4 a f 9 a 6 3
7 3 9 5 2 b 8 1 5 9 d 6 3 4 3 0 2 0 4 5 3
8 5 1 a 2 7 f 9 2 4 c 6 d 8 1 9 1 e 2 b 3
5 5 b 5 4 f c 6 d 8 7 c c 8 9 b 0 4 6 b d
e 2 a b 9 5 c d f 9 4 3 1 c 2 b a 9 f 3 3
0 c 2 1 d 9 f 8 d 0 3 d a b 6 a b 4 6 e 5
```


With this text, we overlapped the output to the actual image, and got a match. With the exception of the first character, the word `lag{` was clear.
Just had to follow the arrows and retrieve the flag.



![ddr solved](https://github.com/uac-ctf/nahamcon2021/raw/main/ddr/ddr-solve.png)


Of course a much better way is to encode the path and update the script so that it follows the arrows and prints the flag.


Flag was ```flag{2a4c690675849c329b2f27fe4c192e}```
