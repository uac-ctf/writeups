# HAXLAB - Flag Leak

The challenge provided a python file implementing a secure calculator. It requires at least python 3.8.5 to run, as it makes use of audit hooks, which has been added along 3.8 and had some fixes in more recent versions.

To run the script we need to create a simple file name ```proprietary.py``` containing the definition of the ```get_flag1()``` function. Its implementation doesn't matter as we cannot use the method to actually retrieve the flag.

Once we run the script, this will be the result.

```
======= HAXLAB - An advanced yet secure calculator =======
Powered by Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110]
>>> 
```

Audit hooks are an interesting feature that was added for auditing events in a application. It can be used to implemented a sandbox, but it is not suited to the purpose and PEP 578 clearly states that
this is not a sandbox.

If we try to access things such as globals, it will fail as the ```open``` event is triggered. 
```
>>> globals()
Operation not permitted: open
>>> print(globals())
Operation not permitted: open
```

Other attempts such as running ```os.system``` or importing _most_ modules, will also be blocked.
Some inputs work. In particular we can list the global objects:
```
exec("for k,v in enumerate(globals()):\n\tprint(k, v)")
0 flag1
1 __builtins__
2 k
3 v
```

Accessing the ```flag1``` directly will not work. Either the output provided is ```REDACTED``` or the ```__getattribute__()``` generates an audit hook, and the instruction is blocked.
Although we cannot use the ```__getattribute__()``` method to extract the flag, we can convert the object to a ```dict``` and then access the values through it.

After some tries, a specific input worked and we got the flag.

```
>>> exec("print(globals()['flag1'].__dict__['-flag1-'][0:-1])")
sdctf{get@ttr_r3ads_3v3ryth1ng}
```
