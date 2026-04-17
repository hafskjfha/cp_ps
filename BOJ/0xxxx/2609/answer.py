import sys

input=sys.stdin.readline

def gcd(a, b):

    while b:

        a, b = b, a % b

    return a

def lcm(a, b):

    return a * b // gcd(a, b)

U=list(map(int,input().split()))

N=max(U)

M=min(U)

g=gcd(N,M)

l=lcm(N,M)

print(g,l,sep='\n')