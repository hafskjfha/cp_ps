def main():
    input=open(0).readline
    n=int(input())
    r=[[0]*n for _ in range(n)]
    for i in range(n):
        a=input().strip()
        for j in range(n):
            if a[j].isdecimal():
                m=int(a[j])
                r[i][j]=-1
                for x,y in [(j+1,i),(j-1,i),(j,i+1),(j,i-1),(j+1,i+1),(j-1,i+1),(j+1,i-1),(j-1,i-1)]:
                    if 0<=x<n and 0<=y<n and r[y][x]!=-1:
                        r[y][x]+=m
    p=[]
    for b in r:
        d=[]
        for c in b:
            if c==-1:
                d.append('*')
            elif c<10:
                d.append(str(c))
            else:
                d.append('M')
        p.append(''.join(d))
    print('\n'.join(p))
main()