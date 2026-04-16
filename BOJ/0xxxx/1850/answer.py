import sys

def Euclidean(a, b):

    while b != 0:

        [a, b] = [b, a%b]

    return a

x,y=map(int,input().split())

if x<y:x,y=y,x

for _ in range(Euclidean(x,y)):sys.stdout.write('1')