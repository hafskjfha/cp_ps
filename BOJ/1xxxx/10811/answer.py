def main():
    input=open(0).readline
    n,m=map(int,input().split())
    a=[*range(1,n+1)]
    for _ in range(m):
        i,j=map(int,input().split())
        a[i-1:j]=reversed(a[i-1:j])
    print(*a)

main()