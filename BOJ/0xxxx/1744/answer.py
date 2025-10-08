def main():
    input=open(0).readline
    n=int(input())
    a=sorted([int(input())for _ in range(n)])
    neg,pos=[],[]
    get0=False
    ans=0
    for x in a:
        if x<0:neg.append(x)
        elif x>0:pos.append(x)
        else: get0=True
    while len(pos)>1:
        p1,p2=pos.pop(),pos.pop()
        if 1 in (p1,p2):
            ans+=p1+p2
            break
        ans+=p1*p2
    ans+=sum(pos)
    for i in range(0,len(neg),2):
        if i==len(neg)-1:break
        ans+=neg[i]*neg[i+1]
    if len(neg)%2 and not get0:
        ans+=neg[-1]
    print(ans)
main()
