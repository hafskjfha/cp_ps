def main():
    input=open(0).readline
    d=set(i*i for i in range(1,10**6,2))
    for _ in range(int(input())):
        n=int(input())
        a=[*range(1,n+1)]
        for i in range(n-1):
            if a[i]+a[i+1] in d:
                a[i-1],a[i]=a[i],a[i-1]
        print(*a)
main()