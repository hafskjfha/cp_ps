def main():
    input=open(0).readline
    n=int(input())
    a=[[]for _ in range(n)]
    for i in range(n):
        _,*x=map(int,input().split())
        for y in x:
            a[y-1].append(i+1)
            
    for b in a:
        print(len(b),*b)

main()