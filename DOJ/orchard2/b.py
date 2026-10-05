import sys
from collections import defaultdict
from math import *

input=sys.stdin.readline

def solve():
    n=int(input())
    s=[*input().strip()]
    ans=0
    dd=defaultdict(int)
    for i in range(0,2*n,2):
        dd[s[i]+s[i+1]]+=1
        if s[i]==s[i+1]:n-=1
    #print(dd)
    for x,y in [('AB','BA'),('AC','CA'),('BC','CB')]:
        n-=min(dd[x],dd[y])*2
        ans+=min(dd[x],dd[y])
    print(ans+ceil(n/2))

def main():
    t=1#int(input())
    for _ in range(t):
        solve()
main()