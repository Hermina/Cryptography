import math
from math import floor
x=123425
p=1559
q=8101
n=p*q
fi=n-p-q+1
e=65537
##e=7
##n=33
v=[1,0,fi,0,1,e]
while (v[5]>0):
    q=floor(v[2]/v[5])
    vt=[v[3],v[4],v[5],v[0]-q*v[3],v[1]-q*v[4],v[2]-q*v[5]]
    v=vt
print v
#(e,d)=1 mod fi

d=748673

y=1
eb=bin(e)[2:]
print eb
for i in range(len(eb)):
    y=(y*y)%n
    if (eb[i]=='1'):
        y=(y*x)%n
print y

l=1
db=bin(d)[2:]
for i in range(len(db)):
    l=(l*l)%n
    if (db[i]=='1'):
        l=(l*y)%n
print l
