a,b=map(int,open(0))
c=b
print(a,b,sep='\n')
while c>0:
    print(a*(c%10))
    c//=10
print(a*b)