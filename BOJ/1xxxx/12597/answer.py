from math import ceil
input=open(0).readline
for T in range(1,int(input())+1):
    n,t=map(int,input().split())
    e=int(input())
    c={i:[]for i in range(1,n+1)}
    m={}
    for _ in range(e):
        h,p=map(int,input().split())
        if p>0:c[h].append(p)
        m[h]=m.get(h,0)+1
    a=[]
    for i in range(1,n+1):
        if i==t or i not in m:a.append("0");continue
        e=m[i]
        s=b=0
        for x in sorted(c[i],reverse=True):
            s+=x
            b+=1
            if s>=e:break
        if s<e:print(f"Case #{T}: IMPOSSIBLE");break
        else:a.append(str(b))
    else:print(f"Case #{T}: {' '.join(a)}")