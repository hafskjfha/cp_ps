from collections import deque

def main():
    input=open(0).readline
    n=int(input())
    taka=sorted([[*map(int,input().split())]for _ in range(n)],key=lambda x:(x[1],x[0]))
    table=[0]*n
    for i in range(n-1,-1,-1):
        h,x=taka[i]
        table[i]=max(0 if i+1==n else table[i+1],h)
    
    tindex=0
    q=int(input())
    ans=[None]*q
    rq=sorted(enumerate(map(int,input().split())),key=lambda x:x[1])
    
    for i in range(q):
        j,t=rq[i]
        while tindex<n and taka[tindex][1]<=t:
            tindex+=1
        ans[j]=table[tindex]
    
    print("\n".join(map(str,ans)))
    
    


main()