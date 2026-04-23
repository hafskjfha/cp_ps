i=input
c=int(i())
i()
[exit(print(x,c//x))for x in sorted(map(int,i().split()))if c%x==0]