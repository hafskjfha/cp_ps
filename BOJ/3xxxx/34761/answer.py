n=int(input())
a=[*map(int,input().split())]
b=[*map(int,input().split())]
print('YNEOS'[a[:n]!=b[:n]or len(set(b)-set(a))>0::2])