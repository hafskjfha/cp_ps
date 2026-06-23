def main():
    input=open(0).readline
    
    n=int(input())
    jaguars=[*map(int,input().split())]
    
    mt=min(jaguars)
    
    ans=0
    for x in jaguars:
        if (x-mt)%2==1:
            return print(-1)
        ans+=(x-mt)//2
    print(ans)


main()