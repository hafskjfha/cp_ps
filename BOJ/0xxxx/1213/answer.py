c={}
for x in input():c[x]=c.get(x,0)+1
r=[]
odd=None
for x,n in sorted(c.items(),key=lambda x:x[0]):
    if n%2:
        if odd is None:
            odd=x
            r.append(x*(n//2))
        else:exit(print("I'm Sorry Hansoo"))
    else:
        r.append(x*(n//2))
print(''.join(r)+(odd or "")+''.join(r[::-1]))