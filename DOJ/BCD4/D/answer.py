import sys

def main():
    INF=float('inf')
    input=sys.stdin.readline
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    
    submina,submaxa=subf(a,n,'m'),subf(a,n,'M')
    subminb,submaxb=subf(b,m,'m'),subf(b,m,'M')
    
    print(max(
        submaxa*submaxb,
        submina*subminb,
        submina*submaxb,
        submaxa*subminb
    ))


def subf(arr,n,k):
    fun=min if k=='m' else max
    res=arr[0]
    temp=arr[0]
    
    for i in range(1,n):
        x=arr[i]
        temp=fun(x,temp+x)
        
        if k=='M':
            if temp > res:res=temp
        else:
            if temp < res:res=temp
    
    return res
        
    
main()