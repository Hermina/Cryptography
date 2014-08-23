import nltk
import time
#rjecnik profesora Igalyja, javno dostupan na http://www.igaly.org/rjecnik-hrvatskih-jezika/pages/preuzimanje.php?lang=EN
f=open("rjecnik.txt","r")

rj=[]
r1="VYFIUSCU"
r2="YZBGACWW"
r1=r1.lower()
r2=r2.lower()

def broj(c):
    return ord(c)-ord('a')

def slovo(c):
    c=c%26
    return chr(c+ord('a'))

for i in range(530000):
    line=f.readline()
    vector=line.split()
    rj.append(vector[0])
sk=set(rj)
f.close()

def kljuc(sifrat,otv):
    rj=[slovo(broj(sifrat[i])-broj(otv[i%len(otv)])) for i in range(len(sifrat))]
    kljuc=""
    for i in range(len(rj)):
        kljuc=kljuc+rj[i]
    return kljuc

def desifriraj(sl,kljuc):
    rj=[slovo(broj(sl[i])-broj(kljuc[i%len(kljuc)])) for i in range(len(sl))]
    desifrat=""
    for i in range(len(rj)):
        desifrat=desifrat+rj[i]
    return desifrat

def main():
    #time.clock()
    for i in range(len(rj)):
        if len(rj[i])==8:
            k1=kljuc(r1,rj[i])
            k2=kljuc(r2,rj[i])
            if desifriraj(r1,k2) in sk or desifriraj(r2,k1) in sk:
                print rj[i]
    #print time.clock()

if __name__ == "__main__":
    main()
