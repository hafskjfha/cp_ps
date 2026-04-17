def main():
    import sys
    from collections import deque
    input=sys.stdin.readline
    inf=float('inf')
    n,m=int(input()),int(input())
    vi=[0]*(n+1)
    fgr=[[inf]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        fgr[i][i]=0
    ngr={i:[]for i in range(1,n+1)}
    for _ in range(m):
        u,v=map(int,input().split())
        fgr[u][v]=1
        fgr[v][u]=1
        ngr[u].append(v)
        ngr[v].append(u)
    gp=[]
    for i in range(1,n+1):
        if vi[i]==0:
            gro=[i]
            q=deque(gro)
            while q:
                nd=q.popleft()
                for nnd in ngr[nd]:
                    if vi[nnd]==0:
                        vi[nnd]=1
                        gro.append(nnd)
                        q.append(nnd)
            gp.append(gro)
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                fgr[j][k]=min(fgr[j][k],fgr[j][i]+fgr[i][k])
    print(len(gp))
    ress=[]
    for sgp in gp:
        r,m=None,inf
        for p in sgp:
            mmax=0
            for i in sgp:
                mmax=max(fgr[p][i],mmax)
            if mmax<m:
                r=p
                m=mmax
        ress.append(r)
    print('\n'.join(map(str,sorted(ress))))
main()