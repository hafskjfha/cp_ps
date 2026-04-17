def main():
    a=[[*map(int,input().split())] for _ in range(9)]
    m=-1
    x,y=0,0
    for i in range(9):
        for j in range(9):
            if a[i][j]>m:
                m=a[i][j]
                x,y=j,i
    print(m)
    print(y+1,x+1)
main()


