def all_count(ac,base):
    if base in (0,1) or ac==0:return str(ac)
    s="0123456789"
    r=[]
    while ac:
        ac,mod=divmod(ac,base)
        r.append(s[mod])
    return "".join(r[::-1])
def main():
    d={x:c for x,c in zip('HTCKG',map(int,input().split()))}
    m=int(input())
    v=d.values
    ac=sum(v())
    for _ in range(m):
        for x,c in zip('HTCKG',map(int,input().split())):
            d[x]-=c
        print(all_count(sum(v()),ac%10)+"7H")
        ac=sum(v())
        print("".join([x for x,c in sorted(d.items(),key=lambda x:(-x[1],x[0]))if c])or"NULL")

main()