from pwn import *
from randcrack import RandCrack
import time

cracker = RandCrack()

if __name__ == "__main__":
    
    cracker = RandCrack()
    r = pwnlib.tubes.remote.remote("challenge.nahamcon.com", 31000)
    r.send("1");

    for i in range(1000):
        r.sendline("2");
        result = r.recv().decode('latin')
        value = int(result.split("\n")[1])
        print(i)
        try:
            cracker.submit(value)
            predict = cracker.predict_getrandbits(32)
            print(f"Predict: {predict}")
            break
        except:
            pass
    
    r.sendline("3");
    r.send(f"{predict}\n")
    print(f"Result: {r.recv()}")



