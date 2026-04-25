def main():
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    su=sum(a)
    ans=-1 if su<m else 1
    if ans!=-1:
        for i in range(n):
            su-=a[i]
            if su<m:
                break
            ans+=1
    print(ans)
main()
