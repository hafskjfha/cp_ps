def main():
    import sys
    input=sys.stdin.readline
    t=int(input())
    for _ in " "*t:
        n,l,f=map(int,input().split())
        words=input().split()
        patten={}
        for word in words:
            patten[word[l-f:]]=patten.get(word[l-f:],0)+1
        print(sum([v//2 for v in patten.values()]))
main()