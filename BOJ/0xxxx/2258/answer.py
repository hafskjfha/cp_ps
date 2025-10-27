def main():
    input=open(0).readline
    INF=float('inf')
    n,m=map(int,input().split())
    meat=sorted((tuple(map(int,input().split()))for _ in range(n)),key=lambda x:(x[1],-x[0]))
    now_w=now_c=0
    lc=-1
    min_cost=INF
    for w,c in meat:
        now_w+=w
        if lc==c:
            now_c+=c
        else:
            now_c=c
        lc=c
        if now_w>=m:    
            min_cost=min(min_cost,now_c)
    print([min_cost,-1][min_cost==INF])
main()