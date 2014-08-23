import nltk
tekst="RVDNUOFSIASKKTKZEAUECLAKFKTAIEOJJJLUAEMARSIETDIEIJPLTSMIESVFADNLKAIBIROISJS"
x=15
y=5
sam=["A","E","I","O","U"]
bigrami=["AK","AN","AS","AT","AV","CI","DA","ED","EN","IC","IJ","IN","IS","JA","JE","KA","KO","LI","NA","NE","NI","NO","OD","OJ","OS","OV","PO","PR","RA","RE","RI","ST","TA","TI","VA","ZA"]

def odvoji_po_indeksu(sl, ind):
    raz_sl=[]
    pom=[]
    for i in range(ind):
        for j in range(i,len(sl),ind):
            pom.append(sl[j])
        raz_sl.append(pom)
        pom=[]
    return raz_sl

def po_stupcima(sl, ind):
    st=[]
    pom=[]
    for k in range(len(sl)/ind):
        for i in range(k*ind,ind+k*ind):
            pom.append(sl[i])
        st.append(pom)
        pom=[]
    return st

def ispisi_omjer(slova):
	a=0
	b=0
	omjer=[]
	pom=[]
	for i in range(len(slova)):
		for j in range(len(slova[0])):
			if slova[i][j] in sam:
				a=a+1
			else:
				b=b+1
		pom.append(a)
		pom.append(b)
		print a, b
		print slova[i]
		a=0
		b=0
	omjer.append(pom)
		

def main():
    sl=[]
    for char in tekst:
        if char.isalpha():
            sl.append(char)
	
    slova1=odvoji_po_indeksu(sl,x)
    slova2=odvoji_po_indeksu(sl,y)
    ispisi_omjer(slova1)
    print "____________"
    ispisi_omjer(slova2)
    slova=slova1
    
    matrica=[]
    m=0
    for i in range(len(slova[0])):
        pom=[]
        for j in range(len(slova[0])):
            br=0
            for k in range(len(slova)):
                if (slova[k][i]+slova[k][j]) in bigrami:
                    br=br+1
            pom.append(br)
            if m<br:
                m=br
        matrica.append(pom)

    stupci=po_stupcima(sl,x)
    st=[]
    print "Najvjerojatniji parovi stupaca:"
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if matrica[i][j]==m:
                print i, j
    print "Matrica cestih bigrama:"
    for i in range(len(matrica)):
        print matrica[i][:]
    #pogadamo permutaciju
    st.append(stupci[1])
    st.append(stupci[4])
    st.append(stupci[2])
    st.append(stupci[3])
    st.append(stupci[0])
    
    for i in range(len(stupci[0])):
        print st[0][i]+st[1][i]+st[2][i]+st[3][i]+st[4][i]

if __name__ == "__main__":
    main()
