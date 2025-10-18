def dfs(gr,di,sc,x):
    stack=[(x,sc[x])]
    while stack:
        x,w=stack.pop()
        for a in gr[x]:
            if di[a]==-1:
                b=sc[a]
                di[a]=w+b
                stack.append((a,w+b))
    return di

def main():
    import sys
    input=sys.stdin.readline
    N=int(input())
    gr=[[]for _ in range(N+1)]
    sc=[0,*map(int,input().split())]
    for _ in range(N-1):
        a,b=map(int,input().split())
        gr[a].append(b)
        gr[b].append(a)
    d1=[-1]*(N+1)
    d2=[-1]*(N+1)
    d1[1]=sc[1]
    d1=dfs(gr,d1,sc,1)
    #print(d1)
    j,k=d1[1],1
    for i in range(1,N+1):
        if d1[i]>j:
            j,k=d1[i],i
    d2[k]=sc[k]
    dfs(gr,d2,sc,k)
    ans,node=0,k
    for i in range(1,N+1):
        if ans<d2[i]:
            ans,node=d2[i],i
    
    print(ans,min(k,node))

main()