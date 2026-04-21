def main():
    import sys
    input=sys.stdin.readline
    n=int(input())
    T=S=0
    ih=[[]for _ in range(366)]
    oh=[[]for _ in range(366)]
    ld=0
    for _ in range(n):
        c,s,e=input().split()
        ih[int(s)-1].append(c)
        oh[int(e)-1].append(c)
        ld=max(int(e)-int(s),ld)
    op=mp=nf=nfp=0
    for i in range(366):
        for c in ih[i]:
            if c=="T":
                T+=1
            else:
                S+=1
        op+=1if S or T else 0
        mp=max(mp,S+T)
        nf+=1if S and T and S==T else 0
        nfp=max(nfp,S+T)if S and T and S==T else nfp
        for c in oh[i]:
            if c=="T":
                T-=1
            else:
                S-=1
        
    print(op,mp,nf,nfp,ld+1)
main()