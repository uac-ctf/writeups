This challenge provided a python script named ```server.py``` which contains the a program that validates commands before execution.
The validation is made by comparing the digest of the command against a fixed list of commands: ```['ls', 'cat flag-1.txt']```

By analysing the code we notice that the command may be in the form ```command# padding``` and only the command will be executed. Also, when a command is successfully executed, the digest of the entire payload is added to the list of allowed commands.

The consequence is that if we have two payloads, with different commands, but with equal hashes, providing the commands in sequence will allow execution of the second. Even if the second is not on the list of allowed commands.

For this to be practical we need to find two payloads so that ```MD5(command1#padding1) == MD5(command2#padding2)```. This is a chosen prefix attack and can be executed with ```HashClash``` or a similar tool. It is also an very costly attack, requiring a lot of computation effort.

A similar attack is the Identical Prefix, where we have two prefixes that are almost the same, except for a small variation. This attack is must more feasible, as the payloads can be generated in a very short time. However, current tools require a specific difference between the prefixes, as the only change must be on position 10, where the second payload will have the value of this byte increased by 1.

Considering that our command is ```cat flag-1.txt``` and the desired command is ```cat flag-2.txt``` and that the 10th byte is ```1``` or ```2``` we meet the requirements for the attack.

Using ```hashclash``` we create a prefix with ```cat flag-1.txt``` and use the ```poc_no.sh``` script. After some time we are left with two payloads that hash to the same value, but with different contents.

```
$ md5sum payload*
29179ce788fc0d3ae16f4e3fc6a73c6f  payload1
29179ce788fc0d3ae16f4e3fc6a73c6f  payload2

$ shasum payload*
296b8b4cf08f194a97e223c92c0bd6bf506d6daa  payload1
078856727c724988eaf785b8f75c52e888e74d10  payload2

```

The payloads need to be converted to base64 and then used in sequence. The first will cat flag1.txt, and the second flag2.txt. 

```
nc unix.sdc.tf 1337
Welcome to the secure playground! Enter commands below
b64
Enter command in base64> Y2F0IGZsYWctMS50eHQjCoo1Cpr4CNMtgiwFzMbbJ027OjIElzDLdH4n+kFVyEG0C/h+rxLQWo9E7hIt1w4uBOoUBwToX7X+5dGzyP1CRToxy65itlGzRAxRNRLykp9b7zwfQ2jJoZoyK18ne+52Ou5Cr5oeeKu7Z/50+FLvBH0=
ftcds{I_dare_y0u_subm1t_THIS!}

b64
Enter command in base64> Y2F0IGZsYWctMi50eHQjCoo1Cpr4CNMtgiwFzMbbJ027OjIElzDLdH4n+kFVyEG0C/h+rxLQWo9E7hIt1w4uBOoUBwToX7X+5dCzyP1CRToxy65itlGzRAxRNRLykp9b7zwfQ2jJoZoyK18ne+52Ou5Cr5oeeKu7Z/50+FLvBH0=
sdctf{MD5_iS_DeAd!L0ng_l1v3_MD5!}
```
