def main():
    n,k=map(int,input().split())
    a=sorted(map(int,input().split()))
    print(a[k-1])
main()