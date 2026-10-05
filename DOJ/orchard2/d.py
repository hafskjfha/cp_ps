import sys
ceil = lambda a, b: (a + b - 1) // b

input=sys.stdin.readline

def solve():
    r,g,k=map(int,input().split())
    if r>g:r,g=g,r
    rr,gg=ceil(r,2),ceil(g,2)
    
    #print(gg-1,r,(gg+1)*2)
    if gg-1<=r<=(gg+1)*2:
        if rr==gg:
            if 2*rr-1<=k:
                print("Yes")
            else:
                print("No")
        else:
            
            if 2*(gg-1)<=k:
                print("Yes")
            else:
                print("No")
    else:
        print("No")

def main():
    t=int(input())
    for _ in range(t):
        solve()
main()