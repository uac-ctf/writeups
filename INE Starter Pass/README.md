# NahamCon2021 INE (Starter Pass) Writeup

500 points - Scripting - 111 Solves - easy

```
Thanks to INE for helping sponsor NahamCon!

You might find some good stuff here ;) https://checkout.ine.com/starter-pass

Perform some reconnaissance on their online presence and find a flag you can submit for points :) 
```


## Solve

The challenge presents a message related to the [INE](https://ine.com/) company. Given the previous info only one person solved it until the challenge's name was change and it was given a new website link. The name was changed to INE (Starter Pass) where it hints to a more particular part of the INE's online presence and the new link [INE Starter Pass](https://checkout.ine.com/starter-pass) confirms it.

In the previous link presented if we inspect the elements we can see a div called "register__analytics". Inside of that div there are more nested divs until we find a paragraph <p> and a <span> and finally inside of that span we see the flag, in a way. 

![ine](https://github.com/uac-ctf/nahamcon2021/blob/main/INE-Starter-Pass/ine.png)

We can see that the string ```ZmxhZ3syOWZhMzA1YWFmNWUwMWU5ZWRjZjAxNDJlNGRkY2RiOX0=``` isn't in the normal flag{...} format, but we can also see that the string ends with an "=". Maybe base64? By using an online base64 decoder we confirm our assumption, it is base 64.

Flag was ```flag{29fa305aaf5e01e9edcf0142e4ddcdb9}```

