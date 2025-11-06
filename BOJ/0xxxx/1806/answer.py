def main():
    input=open(0).readline
    n,s=map(int,input().split())
    a=[*map(int,input().split())]
    ans=n+1
    psum=[0]*(n+1)
    for i in range(n):
        psum[i+1]=psum[i]+a[i]
    i,j=0,0
    while i<=j and j<n+1:
        x=psum[j]-psum[i]
        if x<s:
            j+=1
        else:
            ans=min(ans,j-i)
            i+=1
    print([0,ans][ans!=n+1])
main()