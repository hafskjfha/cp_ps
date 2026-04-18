def main():
    input=open(0).readline
    while 1:
        t=input()
        if not t: break
        n,*a=map(int,t.split())
        s=set(abs(a[i]-a[i+1])for i in range(n-1))
        k=set(i for i in range(1,n))
        print('Not jolly'if s!=k else 'Jolly')
main()