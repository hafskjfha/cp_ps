def main():
    input=open(0).readline
    n,k=map(int,input().split())
    a=[]
    for _ in range(n):
        _,*t=input().split()
        a.append(t)
    cs=[*map(int,input().split())]
    
    for x,y in zip(a,cs):
        if k<=len(x)*y:
            z=k%len(x)
            return print(x[z-1])
        else:
            k-=len(x)*y
    

main()