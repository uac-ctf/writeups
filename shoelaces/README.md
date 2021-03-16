# NahamCon2021 Shoelaces Writeup

50 points - Warmups - 2248 Solves - easy

```
Do you double-knot your shoelaces? You gotta keep'em tied!
```

## Solve

Run this command:

`strings shoelaces.jpg | grep "flag"`

The _strings_ command outputs the (readable) text parts of the file and then _grep_ finds the flag in that sequence of strings.

The output is the flag.

Flag was `flag{137288e960a3ae9b148e8a7db16a69b0}`
