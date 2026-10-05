import sys
input=sys.stdin.readline

def solve():
    n=int(input())
    a=[*map(int,input().split())]
    
    count=[0]*30
    for x in a:
        k=bin(x)[2:][::-1]
        #print(k)
        for i in range(len(k)):
            if k[i]=='1':count[i]+=1
    
    for i in range(30):
        if count[i]%2==0:
            for j in range(n):
                a[j]&=~(1<<i)
    for x in a:
        k=bin(x)[2:][::-1]
        #print(k)    
    
    #print(count)
    print(max(a))

def main():
    t=int(input())
    for _ in range(t):
        solve()
main()