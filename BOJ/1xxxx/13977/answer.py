D=1000000007
fact=[1]*4000001
for i in range(2,4000001):
    fact[i] = (fact[i-1]*i) % D
import sys
input=sys.stdin.readline
for _ in range(int(input())):
	N,K=map(int,input().split())
	M=pow(fact[N-K]*fact[K],D-2,D)
	print((fact[N]*M)%D)