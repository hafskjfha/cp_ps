n=int(input())
a,b="",""
for i in range(1,n+1):
    if i==n:
        a+="*"*(2*n-1)+"\n"
        continue
    a+=" "*(n-i)+"*"*(2*i-1)+"\n"
    b=" "*(n-i)+"*"*(2*i-1)+"\n"+b
print(a+b)