def main():
    n,m=map(int,input().split())
    a=map(int,input().split()).__next__
    p=[0]*n
    p[0]=a()
    for i in range(1,n):
        p[i]=p[i-1]+a()
    c=[0]*m
    for d in p:
        c[d%m]+=1
    ans=c[0]
    for k in c:
        ans+=(k*(k-1))//2
    print(ans)
main()
