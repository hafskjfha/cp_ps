def main():
    input=open(0).readline
    h,w,k=map(int,input().split())
    g=[[*map(int,input().strip())]for _ in range(h)]
    ps=[[0]*(w+1)for _ in range(h+1)]
    for i in range(1,h+1):
        for j in range(1,w+1):
            ps[i][j]=g[i-1][j-1]+ps[i-1][j]+ps[i][j-1]-ps[i-1][j-1]
    
    ans=0
    
    for x1 in range(1,h+1):
        for x2 in range(x1,h+1):
            a=[ps[x2][j]+ps[x1-1][0]-ps[x2][0]-ps[x1-1][j]for j in range(w+1)]

            i,j=0,0
            for l in range(w+1):
                i=max(i,l+1)
                j=max(j,l+1)
                while i<=w and a[i]-a[l]<k:i+=1
                while j<=w and a[j]-a[l]<=k:j+=1
                ans+=j-i
            
            # c={0:1}
            # for i in range(1,w+1):
            #     s=a[i]
            #     ans+=c.get(s-k,0)
            #     c[s]=c.get(s,0)+1
                

    
    print(ans)
    
main()