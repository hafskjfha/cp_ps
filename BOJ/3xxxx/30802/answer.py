import math
N=int(input())
w=[*map(int,input().split())]
T,P=map(int,input().split())
print(sum(map(lambda x:math.ceil(x/T),w)))
print(N//P,N%P)