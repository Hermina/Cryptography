a=['8c','04','f9','f0']
b=['e2','d5','ee','9c']

#a=['02','01','01','03']
#b=['0e','09','0d','0b']

def ostatak(s):
    p=int('100011011',2)
    while (len(bin(s))-len(bin(p))>=0):
        s=s^(p<<(len(bin(s))-len(bin(p))))
    return s

def pomnozi(x,y):
    sum=0
    x=bin(int(x,16))[2:]
    y=bin(int(y,16))[2:]
    for i in range(len(x)):
        sum=sum^(int(y,2))*int(x[len(x)-i-1])*pow(2,i)
    sum=ostatak(sum)
    print x, y, bin(sum)[2:]
    return sum

A=[]
pom=[]
for i in range(4):
    pom.append(a[i])
    pom.append(a[(i-1)%4])
    pom.append(a[(i-2)%4])
    pom.append(a[(i-3)%4])
    A.append(pom)
    pom=[]

d=[]
s=0
for i in range(4):
    for j in range(4):
        s=s^pomnozi(A[i][j],b[j])
    d.append(hex(s)[2:])
    s=0

print d

print bin(ostatak(int('11100001100111',2)))[2:]
