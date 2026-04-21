def main():
    import sys
    input=sys.stdin.readline
    n,m=map(int,input().split())
    x,y=-1,-1
    for i in range(n):
        s=input().split()
        for j in range(m):
            if s[j]=="1":
                if x==-1:
                    x,y=j,i
                else:
                    print(abs(i-y)+abs(j-x))
                    break
                    
main()