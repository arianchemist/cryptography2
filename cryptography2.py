import hashlib

import random

def simpleDE(n):
    l = n[0] + n[0] + n[1] + n[0]
    print(l)

def SSXD(v):
    l2 = v[0] + v[3] + v[6] + v[2] + v[1] + v[5] + v[4]
    print(l2)

def simplehash(k):
    # md5 hash
    vv = hashlib.md5()
    vv.update(b"{k}")
    print(vv.digest())
    # hex digest
    print("hex")
    print(vv.hexdigest())

def GGT(f):
    Ns = hashlib.md5()
    Ns.update(b"{f}")
    CoK = Ns.hexdigest()
    CoK = CoK + "fc" + CoK + "avvc" + CoK
    print(CoK)

def simplesha256(a):
    Aa = hashlib.sha256()
    Aa.update(b"{a}")
    print(Aa.digest())
    # hex digest
    print("hex")
    print(Aa.hexdigest())

#def CCSX(s):
#    s = s + s + s + "stf" + s
#    VXH = hashlib.sha256()
#    VXH.update(b"{s}")
#    print(VXH.hexdigest())

def rRA(w):
    abc = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
    llf = random.choice(abc)
    llf2 = random.choice(abc)
    llf3 = random.choice(abc)
    ssa = w[0] + llf + w[1] + w[2] + w[3] + llf2 + w[4] + w[5] + w[6] + llf3 + w[7]
    print(ssa)

def VVjJ(q):
    abc2 = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]
    h3 = random.choice(abc2)
    h6 = random.choice(abc2)
    h8 = random.choice(abc2)
    xxg = q[0] + h3 + q[7] + q[5] + h6 + q[3] + h8 + q[2] + q[4] + q[1] + q[6]
    print(xxg)

print("""
a for simpleDE
b for SSXD
c for simplehash
d for GGT
e for simplesha256
f for rRA
g for VVjJ
""")

while True:
    Gv = str(input("enter option > "))
    if Gv == "a":
        T = str(input("enter your string : "))
        simpleDE(T)
    elif Gv == "b":
        T1 = str(input("enter your string : "))
        SSXD(T1)
    elif Gv == "c":
        T2 = str(input("enter your string : "))
        simplehash(T2)
    elif Gv == "d":
        T3 = str(input("enter your string : "))
        GGT(T3)
    elif Gv == "e":
        T4 = str(input("enter your string : "))
        simplesha256(T4)
    elif Gv == "f":
        T5 = str(input("enter your string : "))
        rRA(T5)
    elif Gv == "g":
        T6 = str(input("enter your string : "))
        VVjJ(T6)
