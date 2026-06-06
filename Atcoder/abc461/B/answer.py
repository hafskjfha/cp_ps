def main():
    input=open(0).readline
    n=int(input())
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    for i in range(n):
        if b[a[i]-1]!=i+1:return print("No")
    print("Yes")
    
main()