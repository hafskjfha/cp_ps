def main():
    n,m=map(int,input().split())
    w=input().split()
    p=[*map(int,input().split())]
    print(n-len(set(p))+1)

main()