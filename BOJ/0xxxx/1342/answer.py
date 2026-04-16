ans = set()
def back(s,p,m):
    global ans
    if len(s)==0:
        for c in p.keys():
            p[c]-=1
            back(c,p,m)
            p[c]+=1
        return
    elif len(s)==m:
        ans.add(s)
        return
    for c in p.keys():
        if p[c] and s[-1]!=c:
            p[c]-=1
            back(s+c,p,m)
            p[c]+=1


def main():
    global ans
    from collections import Counter
    s=input()
    p=Counter(s)
    back("",p,len(s))
    print(len(ans))
main()