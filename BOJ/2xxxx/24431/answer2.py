def main():
    import sys
    input=sys.stdin.readline
    t=int(input())
    for _ in " "*t:
        n,l,f=map(int,input().split())
        words=input().split()
        ans=0
        cc=set([w[l-f:]for w in words])
        for patten in cc:
            temp=0
            for word in words:
                if word[l-f:]==patten:
                    temp+=1
            ans+=temp//2
        print(ans)
main()