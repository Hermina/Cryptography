import nltk

tekst="UCOOA VWVJO OVGVF KRVNB BPQQB FRYMJ MFGZZ RGZQG WGBJO UAMXJ HUAVN EXKOF OFJXQ AXDSF VREFC QZZIK CMZRY ZXOWG BJOUR VGVYU TZDFD UTZTC TGJVM JYOPJ NJHGD RMVFG HCBTW ZMGHJ HAXBX QOOHI TUIQT ANTSB IGHDC ICIBA SIQZE ZTXIQ T"
niz=[115,15,28,37,84,3,16,8,98,51,36,33,31,66,90,29,0,54,56,48,43,35,0,0,0,23]

#prevodi slovo u odgovarajuci broj
def broj(c):
    return ord(c)-ord('A')

def slovo(c):
    c=c%26
    return chr(c+ord('A'))

def desifriraj(sl,kljuc):
    rj=[slovo(broj(sl[i])-broj(kljuc[i%len(kljuc)])) for i in range(len(sl))]
    desifrat=""
    for i in range(len(rj)):
        desifrat=desifrat+rj[i]
    return desifrat

#vraca 6(duljina kljuca) rjecnika. Rjecnik s indeksom i sadrzi sva slova na pozicijama k, k%6=i, poredana po frekvenciji i njihovu frekvenciju 
def odvoji_po_indeksu(sl):
    raz_sl=[]
    pom=[]
    for i in range(6):
        for j in range(i,len(sl),6):
            pom.append(sl[j])
        raz_sl.append(pom)
        pom=[]
    return [nltk.FreqDist(raz_sl[i]) for i in range(6)]

#analizira frekvencije pojavljivanja slova i vraca najvjerojatniji kljuc
def kljuc(slova):
    m=[0]*6
    ind=[0]*6
    for i in range(6):
        for j in range(26):
            rez=sum([niz[k]*slova[i][slovo(j+k)]*1.0 for k in range(26)])/sum(slova[i].values())
            if (m[i]<rez):
                m[i]=rez
                ind[i]=j
    kljuc=""
    for i in range(6):
        kljuc=kljuc+slovo((26+ind[i])%26)
    return kljuc

def main():
    sl=[]
    for char in tekst:
        if char.isalpha():
            sl.append(char)

    slova=odvoji_po_indeksu(sl)

    k=kljuc(slova)
    print k
    otvoreni=desifriraj(sl,k)
    print otvoreni

if __name__ == "__main__":
    main()

