a=sum(map(lambda x:int(x,2),input().split()))
b=""
if a!=0:
    s="01"
    while a:
        b = s[a%2]+b
        a//=2
print(b or 0)