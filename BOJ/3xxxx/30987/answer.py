def main():
    x1,x2=map(int,input().split())
    a,b,c,d,e=map(int,input().split())
    b=(b-d)//2
    c-=e
    a//=3
    f=lambda a,b,c,x: a*x**3+b*x**2+c*x
    print(f(a,b,c,x2)-f(a,b,c,x1))
main()