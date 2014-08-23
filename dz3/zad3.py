E1 = '000011'
E11 = '110111'
C1= '1000'
E2= '001000'
E22 = '111100'
C2 = '0010'

def xxor(a,b):
    r=''
    for i in range(len(a)):
        r=r+str((int(a[i])+int(b[i]))%2)
    return r

def main():
    E1c=xxor(E1,E11)
    E2c=xxor(E2,E22)
    print E1c,E2c #ok, prepisujemo iz tablice:
    B1=['001001','001100','011001','101101','111000','111101']
    B2=['000100','000101','001110','010001','010010','010100','011010','011011','100000','100101','010110','101110','101111','110000','110001','111010']
    t1=[]
    t2=[]
    for i in range(len(B1)):
        t1.append(xxor(B1[i],E1))
    for i in range(len(B2)):
        t2.append(xxor(B2[i],E2))
    print t1,t2        

if __name__ == "__main__":
    main()
