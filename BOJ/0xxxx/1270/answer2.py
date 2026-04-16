def main():
    import sys
    input=sys.stdin.readline
    N=int(input())
    for _ in range(N):
        T=map(int,input().split())
        j=next(T)
        h=next(T)
        c=1
        u={h:1}
        for i in T:
            u[i]=u.get(i,0)+1
            if i==h:
                c+=1
            else:
                c-=1
                if c==0:
                    h=i
                    c=1
                    
        if u[h]>j//2:
            print(h)
        else:
            print("SYJKGW")

main()