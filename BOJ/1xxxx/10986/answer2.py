def main():
    n,m=map(int,input().split())
    a=map(int,input().split())
    c=[0]*m
    s=0
    for x in a:
        s=(s+x)%m
        c[s]+=1
    ans=c[0]
    for k in c:
        ans+=(k*(k-1))//2
    print(ans)
main()
