def f(a,b,c,n):
    for x in range(n//a+1):
        for y in range((n-a*x)//b+1):
            z=n-a*x-b*y
            if z%c==0 and z>=0:
                return 1
    return 0
print(f(*map(int,input().split())))