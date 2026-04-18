def main():
    from sys import stdin,stdout
    i=1
    input=stdin.readline
    print=stdout.write
    r=[]
    while 1:
        n=int(input())
        if n==0: break
        gr=[*map(int,input().split())]
        a,b,c=float('inf'),gr[1],gr[1]+gr[2]
        for _ in range(n-1):
            gr=[*map(int,input().split())]
            d=min(a,b)+gr[0]
            e=min(a,b,c,d)+gr[1]
            f=min(b,c,e)+gr[2]
            a,b,c=d,e,f
        r.append(f"{i}. {b}")
        i+=1
    print('\n'.join(r))
main()