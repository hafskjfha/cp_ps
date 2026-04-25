def main():
    import sys
    input=sys.stdin.readline
    n=int(input())
    l=set()
    for _ in range(n):
        for i in map(int,input().split()):
            if i in l:
                print(1)
                return
            l.add(i)
    print(0)
main()
        