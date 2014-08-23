import nltk

tekst="VERNAM"
sifrat="HDPQWE"

def broj(c):
    return ord(c)-ord('A')

#vraca determinantu 2*2 matrice mod 26
def det2(x):
    return (x[0]*x[3]-x[1]*x[2])%26

def inverz(x):
    a=det2(x)
    ainv=-1
    for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
        if ((a*i)%26==1):
            ainv=i
    if (ainv==-1):
        print "Nema inverza"
        return [0,0,0,0]
    else:
        pom=[x[3],-x[1],-x[2],x[0]]
        xinv=[(pom[i]*ainv)%26 for i in range(len(pom))]
        return xinv
    
#mnozi dvije 2*2 matrice zapisane kao niz
def pomnozi(x,y):
    k=[]
    for i in range(0,4,2):
        for j in range(2):
            k.append((x[i]*y[j]+x[i+1]*y[j+2])%26)
    return k

def main():
    textub=[int(broj(tekst[i])) for i in range(len(tekst))]
    sifratub=[int(broj(sifrat[i])) for i in range(len(sifrat))]
    a=inverz(textub[0:4])
    if (a!=[0,0,0,0]):
        k=pomnozi(a,sifratub[0:4])
        if (pomnozi(textub[2:6],k)==sifratub[2:6]): print k

if __name__ == "__main__":
    main()
