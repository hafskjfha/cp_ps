def dfs(gr,di,x,w):
    stack=[(x,w)]
    while stack:
        x,w=stack.pop()
        for a,b in gr[x]:
            if di[a]==-1:
                di[a]=w+b
                stack.append((a,w+b))
    return di

def main():
    import sys
    input=sys.stdin.readline
    N=int(input())
    gr=[[]for _ in range(N+1)]
    for _ in range(N):
        t=input().split();t.pop()
        a,*b=map(int,t)
        for i in range(0,len(b),2):
            c,d=b[i],b[i+1]
            gr[a].append((c,d))
    d1=[-1]*(N+1)
    d2=[-1]*(N+1)
    d1[1]=0
    d1=dfs(gr,d1,1,0)
    j=k=0
    for i in range(1,N+1):
        if d1[i]>j:
            k=i
            j=d1[i]
    d2[k]=0
    print(max(dfs(gr,d2,k,0)))

main()