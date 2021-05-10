
# NahamCon2021 Dice Roll Writeup

406 points - Cryptography - 201 Solves - medium

```
When you have just one source of randomness, it's "a die", but when you can have muliple -- it's 'dice!'

NOTE: You are welcome to "brute force" this challenge if you feel you need to. ;)

```


## Solve

The challenge provided a ```dice_roll.py``` file that we can use to analyse how the remote application works.

The program uses Python ```random``` module which is known for not producing quality randomized values.

When the dices are shaken, the random generator is seeded with really random seed from ```/dev/urandom```, but then it uses the standard ```random``` module.

This leads to the possibility of guessing the next value by analysing previously generated numbers. Someone already created a Python module for this: [Python-random-module-cracker](https://github.com/tna0y/Python-random-module-cracker)

Solving the challenge will consist in getting enough information from the remote system, use the cracker to predict the next value, and then retrieve the flag.

The ```solve.py``` script implements this solution. Instead of using a fixed number of iterations, we opted for getting as much as needed until the value could be predicted. Setting the loop to 624 would yield similar results.