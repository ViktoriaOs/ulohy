import random

zoznam=[]
def generuj(n):
    
    for i in range (n):
        zoznam.append(random.randint(5,11))
    print(zoznam)
    return zoznam
#generuj(5)
pass

def sucet_parne(z):
    return sum(cislo for cislo in z if cislo % 2 == 0)
#print("Zoznam:", zoznam)
#print("Súčet:",sucet_parne(generuj(3)))
pass

#z=list(map(int,input("Zadaj random cisla:").split(",")))
def coho_je_viac(z):
    par=sum(1 for cislo in z if cislo%2==0)
    npar=sum(1 for cislo in z if cislo%2!=0)
    if par>npar:
        return "parne"
    elif par<npar:
        return "neparne"
    else:
        return "rovnake"    
#print(coho_je_viac(z))
pass

d=[]
def parne_pozicie(d):
    a=[]
    for i in range(0, len(d),2):
        a.append(d[i])
    return a
#print(parne_pozicie([22,1,93,27,38,59]))
pass

def nie_cisla(b):
    return [x for x in b if not isinstance(x, (int, float))]
#print(nie_cisla(["kuk", 5, "ahoj", -1, 2.5, 4, "None", 7, [2,-12], 8, "servus",11]))
pass

def spolu_do_retazca(b):
    return "".join(str(prvok) for prvok in b)
#print(spolu_do_retazca(["ahoj", 12, -3, "kukuk", 6.45, "True"]))
pass

def zoznam_mocnin(n):
    i=0
    c=[]
    for i in range(1,n+1):
       c.append(i**2)
    return c
print(zoznam_mocnin(6))