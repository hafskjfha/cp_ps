a=[1,1,2,2,2,8]
b=[*map(int,input().split())]
print(" ".join([str(a[i]-b[i]) for i in range(6)]))