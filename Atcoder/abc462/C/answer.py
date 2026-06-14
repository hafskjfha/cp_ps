
def main():
    input=open(0).readline
    n=int(input())
    a=sorted([*map(int,input().split())]for _ in range(n))
    
    ans=0
    
    my=float('inf')
    for x,y in a:
        if y<=my:ans+=1
        my=min(my,y)
        
    print(ans)
    

main()