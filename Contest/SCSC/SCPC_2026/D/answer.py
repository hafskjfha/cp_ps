def main():
    input=open(0).readline
    n,t=map(int,input().split())
    ans=0
    for i in range(n):
        k,*x=map(int,input().split())
        tm=temp=0
        for j in range(min(k,t//n+(i<(t%n)))):
            temp+=x[j]
            tm=max(tm,temp)
        ans+=tm
    print(ans)
    
main()