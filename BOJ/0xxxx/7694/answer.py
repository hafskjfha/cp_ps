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
    while 1:
        x1,y1,x2,y2,x3,y3=map(int,input().split())
        if (x1==y1==x2==y2==0): break
        vertex=[(x1,y1),(x2,y2),(x3,y3)]
        E=0
        x,y=vertex[0]
        for i in range(1,4):
            dx,dy=vertex[i%3]
            E+=gcd(abs(dx-x),abs(dy-y))-1
            x,y=dx,dy
        A=f(vertex)
        E+=3
        ans.append(f"{int(A+1-E/2)}")
    print('\n'.join(ans))

main()