def main():
    from collections import defaultdict
    input=open(0).readline
    p=defaultdict(set)
    n,m=map(int,input().split())
    for _ in range(n):
        s=input().strip()
        p[(s[0],s[-1])].add(s)
    a=0
    for _ in range(m):
        s=input().strip()
        if s in p[(s[0],s[-1])]:
            a+=1
    print(a)
main()

