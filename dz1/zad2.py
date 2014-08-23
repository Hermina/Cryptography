#program vraca sve ngrame i njihov broj pojavljivanja. tada na temelju analize korisnik upisuje dva slova za zamjenu (mala slova) i program vraca sifrirani tekst u kojem su napravljene sve trazene zamjene. u svim tim medukoracima mala slova predstavljaju otvoreni tekst,a velika sifrat.
import nltk
from nltk import bigrams
import sys

tekst="QOPVF WTWIV YWRWE WUWHK RUVNV BTFWF GBFGE PRVSP BCVFP BFIWF GBFWH RUWYB IBIEV UWAWN RPOBB KEVCG BYEPX VUVBC VFPBU WRWKB OVKBC BOVPO XPQWG FKVZF HFGPI PGWEP NOVSV GWCBF GHCKW NPVNE PTHKO UHSWI PCBAB SHEVU WSVVO VXEPN P"
#ispisuje sve ngrame po frekventnosti
def pronadi_najcesce():
    sl=[]
    for char in tekst:
        if char.isalpha():
            sl.append(char)
    slova=nltk.FreqDist(sl);
    bigrami=nltk.FreqDist(bigrams(sl))
    tr=[sl[i]+sl[i+1]+sl[i+2] for i in range(len(sl)-2)]
    trigrami=nltk.FreqDist(tr)
    print "Trigrami..."
    print trigrami.keys()
    print trigrami.values()
    ce=[sl[i]+sl[i+1]+sl[i+2]+sl[i+3] for i in range(len(sl)-3)]
    cetrigrami=nltk.FreqDist(ce)
    print "Cetrigrami..."
    print cetrigrami.keys()
    print cetrigrami.values()
    pe=[sl[i]+sl[i+1]+sl[i+2]+sl[i+3]+sl[i+4] for i in range(len(sl)-4)]
    petrigrami=nltk.FreqDist(pe)
    print "Petgrami..."
    print petrigrami.keys()
    print petrigrami.values()
    se=[sl[i]+sl[i+1]+sl[i+2]+sl[i+3]+sl[i+4]+sl[i+5] for i in range(len(sl)-5)]
    setrigrami=nltk.FreqDist(se)
    print "Sestgrami..."
    print setrigrami.keys()
    print setrigrami.values()
    
    big=[a[0]+a[1] for a in bigrami.keys()]
    bparovi=[(big[i],bigrami.values()[i]) for i in range(len(big))]
    sparovi=[(slova.keys()[i],slova.values()[i]) for i in range(len(slova.keys()))] 
    frslova=[k*1000/float(len(sl)) for k in slova.values()]
    frbigrami =[k*1000/float(len(sl)-1) for k in bigrami.values()]
    print "Bigrami...", bparovi
    print " "
    print "Slova...", sparovi
    print " "
    print frslova

def broj(c):
    return ord(c)-ord('a')

#vrti beskonacnu petlju koja prihvaca parove slova i zamijenjuje ih. petlja se prekida stringom '123'
def trazi():
    tekst2=tekst
    while(1):
        prvi=sys.stdin.readline().strip().split()
        if (prvi==['123']):
            break
        else:
            tekst2=tekst2.replace(prvi[0].upper(),prvi[1])
            print tekst2

def main():
    pronadi_najcesce()
    trazi()
    
if __name__ == "__main__":
    main()

