def main():
    input=open(0).readline
    n=int(input())
    s=input().strip()
    
    ps=[0]*(n+1)
    
    for i in range(n):
        ps[i+1]=ps[i]+(s[i]=='B')
    
    ans=min(ps[-1],n-ps[-1])
    
    for i in range(n):
        ans=min(ans,(i+1)-ps[i+1]+(ps[n]-ps[i+1]),ps[i+1]+(n-i-1)-(ps[n]-ps[i+1]))
    print(ans)


main()