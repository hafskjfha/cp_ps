import sys
input=sys.stdin.readline

def solve():
    a,b=map(int,input().split())
    s,w=map(int,input().split())
    print("YES"if a<=s and b<=w else "NO")

def main():
    t=1#int(input())
    for _ in range(t):
        solve()
main()