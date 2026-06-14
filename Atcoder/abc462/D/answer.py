
def main():
    input=open(0).readline
    n,d=map(int,input().split())
    m=10**6+1
    h=[0]*m
    
    for _ in range(n):
        s,t=map(int,input().split())
        if t-s>=d:
            h[s]+=1
            h[t-d+1]-=1
    
    cur=ans=0
    for i in range(m):
        cur+=h[i]
        ans+=cur*(cur-1)//2
    print(ans)


main()