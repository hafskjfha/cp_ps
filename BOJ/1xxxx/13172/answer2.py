from sys import stdin
input=stdin.readline
S,D=0,int(1e9+7)
for _ in range(int(input())):
        b,a=map(int,input().split())
        b=pow(b,D-2,D)
        S=(S+b*a%D)%D
print(S)