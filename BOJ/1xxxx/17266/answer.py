def sol(a,h):
    if a[1]-a[0] > h or a[-1]-a[-2] > h:
        return 0
    for i in range(1, len(a)-2):
        if (a[i+1]-a[i])/2 > h:
            return 0
    return 1


def main():
    input=open(0).readline
    n,_=int(input()),input()
    k=[0,*map(int,input().split()),n]
    s,e=0,n
    while s<=e:
        mid = (s+e)//2
        if sol(k,mid):
            ans=mid
            e=mid-1
        else:
            s=mid+1
    print(ans)
main()
