def main():
    import sys
    input=sys.stdin.readline
    n,t=map(int,input().split())
    ia=[0]*(100001)
    for _ in range(n):
        for _ in range(int(input())):
            s,e=map(int,input().split())
            ia[s]+=1
            ia[e]-=1
    for i in range(1,100001):
        ia[i]+=ia[i-1]
    su=sum(ia[:t])
    msu=su
    ast=0
    for i in range(t,100001):
        su+=ia[i]-ia[i-t]
        if su>msu:
            msu=su
            ast=i-t+1
    print(ast,ast+t)
main()