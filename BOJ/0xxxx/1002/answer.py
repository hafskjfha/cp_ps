def sol(x1,y1,r1,x2,y2,r2):
    k=(x1-x2)**2+(y1-y2)**2
    r=abs(r1-r2)**2
    if k==0:
        return -1if r1==r2 else 0
    if r<k<(r1+r2)**2:
        return 2
    return 1if k==r or k==(r1+r2)**2 else 0
print(*[sol(*map(int,i.split()))for i in [*open(0)][1:]])