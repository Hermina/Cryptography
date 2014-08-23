# -*- coding: cp1250 -*-
#vraca najfrekventnija slova i bigrame. na temelju njih korisnik pokusava odgonetnuti dva slova. od korisnika se trazi da upise ta dva slova(moraju biti mala slova), te mu program vraca informaciju postoji li kljuc, te ako postoji, njegovu vrijednost i otvoreni tekst
import nltk
from nltk import bigrams
import sys

tekst="AEFFE KODHE ULOKX QOKZH KQUXK NRUCE OKOUH ECWED WHEPZ GFGMG OIWXN EBEEX LUWQW GEXCE LUXCE NUEXN UMGRU PHEON UXUIW HEPZG FGMEN EIRUG NUQZK ZEQZU CWUOU ZGLUI WHEPZ GFGME NI"
def pronadi_najcesce():
    sl=[]
    for char in tekst:
        if char.isalpha():
            sl.append(char)
    slova=nltk.FreqDist(sl);
    bigrami=nltk.FreqDist(bigrams(sl))
    big=[a[0]+a[1] for a in bigrami.keys()]
    bparovi=[(big[i],bigrami.values()[i]) for i in range(len(big))]
    sparovi=[(slova.keys()[i],slova.values()[i]) for i in range(len(slova.keys()))] 
    frslova=[k/1.42 for k in slova.values()]
    frbigrami =[k/1.41 for k in bigrami.values()]
    print "Bigrami...", bparovi
    print "Slova...", sparovi

def broj(c):
    return ord(c)-ord('a')

#za zadana dva para slova vraca kljuc, ako on postoji
def pronadi_parametre(prvi,drugi):
    a=-1
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        for j in range(26):
            if ((i*broj(prvi[0])+j)%26==broj(prvi[1]) and (i*broj(drugi[0])+j)%26==broj(drugi[1])):
                a=i
                b=j
    return a,b

#na temelju kljuca desifrira tekst ili vraca poruku
def pronadi_tekst(a,b):
    if (a==-1):
        print "Nema kljuca"
    else:
        print "Kljuc je:",a,b
        for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
            if ((a*i)%26==1):
                ainv=i
        tekst2=tekst
        for i in range(26):
            tekst2=tekst2.replace(chr(i+ord('A')),chr(((ainv*(i-b))%26)+ord('a')))
        return tekst2

def main():
    pronadi_najcesce()
    print "Unesi slovo i njegov sifrat odvojene razmakom, pa to ponovi za neko drugo slovo u novom redu"
    prvi=sys.stdin.readline().strip().split()
    drugi=sys.stdin.readline().strip().split()
    a,b=pronadi_parametre(prvi,drugi)
    t=pronadi_tekst(a,b)
    print t
    
if __name__ == "__main__":
    main()

