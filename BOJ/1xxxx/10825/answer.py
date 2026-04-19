def f(x):
    y=x.split()
    return y[0],*map(int,y[1:])
I=open(0).readline
print('\n'.join(x[0]for x in sorted([f(I())for _ in range(int(I()))],key=lambda x:(-x[1],x[2],-x[3],x[0]))))