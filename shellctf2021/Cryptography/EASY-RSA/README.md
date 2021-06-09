# Easy-RSA
###### Cryptography - 50 points

```
n = 1763350599372172240188600248087473321738860115540927328389207609428163138985769311
e = 65537
c = 334752481114211949024977428768859353103048624289808755223333038405651136629435
```

Using `RsaCtfTool` with the provided parameters its possible to get the flag

```
$ python3 ./RsaCtfTool.py -n 1763350599372172240188600248087473321738860115540927328389207609428163138985769311 -e 65537 --uncipher 33475248111421194902497742876885935310304862428980875522333303840565113662943528
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmphc8b31w2.
[*] Performing mersenne_primes attack on /tmp/tmphc8b31w2.
 24%|████████████████████████████████████▉                                                                                                                        | 12/51 [00:00<00:00, 183024.17it/s]
[*] Performing fibonacci_gcd attack on /tmp/tmphc8b31w2.
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 248323.42it/s]
[*] Performing pastctfprimes attack on /tmp/tmphc8b31w2.
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 113/113 [00:00<00:00, 2016835.54it/s]
[*] Performing smallq attack on /tmp/tmphc8b31w2.
[*] Performing factordb attack on /tmp/tmphc8b31w2.
[*] Attack success with factordb method !

Results for /tmp/tmphc8b31w2:

Unciphered data :
HEX : 0x00000000007368656c6c7b737769746368696e5f746f5f6173796d6d65747269637d
INT (big endian) : 3111388068276188662361997958100924356274395167698926770307665056326525
INT (little endian) : 3716857967501616239523840250653395077772235796196542527851123201402003116282347520
STR : b'\x00\x00\x00\x00\x00shell{switchin_to_asymmetric}'

```


```
shell{switchin_to_asymmetric}
```

### Attachments
[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
###### 2021 - methane4