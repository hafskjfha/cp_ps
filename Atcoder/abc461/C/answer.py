def main():
    input=open(0).readline
    n,k,m=map(int,input().split())
    gs={}
    gm={}
    for _ in range(n):
        c,v=map(int,input().split())
        gs.setdefault(c,[]).append(v)
        gm[c]=max(gm.get(c,0),v)
    
    for key in gs.keys():gs[key].sort()
    
    sgm=sorted(gm.items(),key=lambda x:-x[1])

    
    ans=0
    for i in range(m):
        c,v=sgm[i]
        gs[c].pop()
        ans+=v
        k-=1
    
    t=[]
    if k:
        for xs in gs.values():
            t.extend(xs)
        t.sort()
        ans+=sum(t[-k:])
        
    
    print(ans)
    
main()