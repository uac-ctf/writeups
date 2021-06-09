# Bruteforce RSA
###### Cryptography - 100 points

```
from Crypto.Util.number import bytes_to_long,inverse,getPrime,long_to_bytes
from secret import message
import json

p = getPrime(128)
q = getPrime(128)

n = p * q
e = 65537 

enc = pow(bytes_to_long(message.encode()),e,n)
print("Encrypted Flag is {}".format(enc))

open('./values.json','w').write(json.dumps({"e":e,"n":n,"enc_msg":enc}))
```


```
{"e": 65537, "n": 105340920728399121621249827556031721254229602066119262228636988097856120194803, "enc_msg": 36189757403806675821644824080265645760864433613971142663156046962681317223254}
```

Using `RsaCtfTool` with the provided parameters its possible to get the flag

```
$ python3 RsaCtfTool.py -n 105340920728399121621249827556031721254229602066119262228636988097856120194803 -e 65537 --uncipher 36189757403806675821644824080265645760864433613971142663156046962681317223254
private argument is not set, the private key will not be displayed, even if recovered.

[*] Testing key /tmp/tmp9i4zz0q7.
[*] Performing mersenne_primes attack on /tmp/tmp9i4zz0q7.
 24%|████████████████████████████████████▉                                                                                                                        | 12/51 [00:00<00:00, 364722.09it/s]
[*] Performing fibonacci_gcd attack on /tmp/tmp9i4zz0q7.
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9999/9999 [00:00<00:00, 254523.44it/s]
[*] Performing pastctfprimes attack on /tmp/tmp9i4zz0q7.
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 113/113 [00:00<00:00, 2069678.39it/s]
[*] Performing smallq attack on /tmp/tmp9i4zz0q7.
[*] Performing factordb attack on /tmp/tmp9i4zz0q7.
[*] Attack success with factordb method !

Results for /tmp/tmp9i4zz0q7:

Unciphered data :
HEX : 0x0000000000007368656c6c6374667b6b33795f73317a655f6d4074746572247d
INT (big endian) : 185453180567955987067286742617490330426585681406450523077485693
INT (little endian) : 56603502101542516885309888740153031607828169274635448325113252619392540213248
STR : b'\x00\x00\x00\x00\x00\x00shellctf{k3y_s1ze_m@tter$}'
```


```
shellctf{k3y_s1ze_m@tter$}
```

### Attachments
[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)
###### 2021 - methane4