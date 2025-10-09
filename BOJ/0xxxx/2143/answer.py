def main():
    t=int(input())
    n=int(input())
    a=[*map(int,input().split())]
    m=int(input())
    b=[*map(int,input().split())]

    a_sum={}
    for i in range(n):
        now=0
        for j in range(i,n):
            now+=a[j]
            a_sum[now]=a_sum.get(now,0)+1

    ans=0
    for i in range(m):
        now=0
        for j in range(i,m):
            now+=b[j]
            ans+=a_sum.get(t-now,0)
    print(ans)

main()