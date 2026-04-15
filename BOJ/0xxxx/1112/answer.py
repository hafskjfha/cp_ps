def s(n,b):
    if n==0:return 0
    r=[]
    u=n<0 and b>0
    n = n if n<0 and b<0 else abs(n)
    while n:
        n,a=divmod(n,b)
        if a<0:
            n+=1
            a+=abs(b)
        r.append(str(a))
    if u: r.append('-')
    return ''.join(r[::-1])
print(s(*map(int,input().split())))