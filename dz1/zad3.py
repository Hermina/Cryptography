#prevodi slovo u odgovarajuci broj
def broj(c):
    return ord(c)-ord('A')

#prevodi broj u odgovarajuce slovo
def slovo(c):
    c=c%26
    return chr(c+ord('A'))

#za proizvoljnu rijec i proizvoljan kljuc vraca sifrat
def sifriraj(rijec,kljuc):
    rj=[slovo(broj(rijec[i])+broj(kljuc[i%len(kljuc)])) for i in range(len(rijec))]
    sifrat=""
    for i in range(len(rj)):
        sifrat=sifrat+rj[i]
    return sifrat

def desifriraj(rijec,kljuc):
    rj=[slovo(broj(rijec[i])-broj(kljuc[i%len(kljuc)])) for i in range(len(rijec))]
    desifrat=""
    for i in range(len(rj)):
        desifrat=desifrat+rj[i]
    return desifrat

def main():
    rijec="PLAYFAIR"
    kljuc="OSAM"
    t=sifriraj(rijec,kljuc)
    t=desifriraj("SARZNBMSQZYDDNP","ZAGREB")
    print t

if __name__ == "__main__":
    main()

