def main():
    input=open(0).readline
    n,x=map(int,input().split())
    mul=[]
    ex0=False
    s=0
    for _ in range(n):
        c,d=input().split()
        d=int(d)
        if c=='+':s+=d
        else:
            if d==0:
                ex0=True
            else:
                mul.append(d)

    if x>0:
        x+=s
        for k in mul:x*=k
    else:
        if ex0:
            x=s
            for k in mul:x*=k
        else:
            x+=s
            if x>0:
                for k in mul:x*=k

    print(x)


main()