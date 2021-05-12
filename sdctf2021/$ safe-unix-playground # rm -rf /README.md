# $ safe-unix-playground # rm -rf /

This challenge provided a python script named ```server.py``` which contains the a program that validates commands before execution.
The validation is made by comparing the digest of the command against a fixed list of commands: ```['ls', 'cat flag-1.txt']```

By analying the code we notice that the command may be in the form ```command# padding``` and only the command will be executed. Also, when a command is successfully executed

