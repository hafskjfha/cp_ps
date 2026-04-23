def main():
    import sys
    input=sys.stdin.readline
    n,m=map(int,input().split())
    a=sorted([int(input()) for _ in range(n)])
    info={}
    r=[]
    for i in range(len(a)):
        info[a[i]]=info.get(a[i],i)
    for _ in range(m):
        r.append(str(info.get(int(input()),-1)))
    sys.stdout.write('\n'.join(r))
    
main()