def main():
    input=open(0).readline
    n=int(input())
    a=[]
    for _ in range(n):
        _,*x=input().split()
        a.append(x)
    i,j=map(int,input().split())
    print(a[i-1][j-1])
    

main()