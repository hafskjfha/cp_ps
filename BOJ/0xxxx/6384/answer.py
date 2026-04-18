def f(poly):
    area = 0
    n=len(poly)
    for i in range(n):
        x1,y1=poly[i]
        x2,y2=poly[(i+1)%n]
        area+=(x1*y2)-(x2*y1)
    return abs(area)/2

def main():
    from math import gcd
    input=open(0).readline
    ans=[]
    for t in range(int(input())):
        ans.append(f'Scenario #{t+1}:')
        x,y=0,0
        vertex=[(x,y)]
        E=0
        M=int(input())
        for _ in range(M):
            dx,dy=map(int,input().split())
            E+=gcd(abs(dx),abs(dy))-1
            x,y=x+dx,y+dy
            vertex.append((x,y))
        A=f(vertex[:-1])
        E+=M
        ans.append(f"{int(A+1-E/2)} {E} {A:.1f}\n")
    print('\n'.join(ans).strip())

main()