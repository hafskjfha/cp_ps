def main():
    n,k,m=map(int,input().split())
    a=[*map(int,input().split())]
    print(a[m-1]if m<=n else sorted(a)[k-1])

main()