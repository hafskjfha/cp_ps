def main():
    input=open(0).readline
    n=int(input())
    c=int(input())
    f=[[*map(int,input().split())]for _ in range(n)]
    ans=0
    for ts in range(max(f,key=lambda x:x[0])[0]*n+1):
        cost=ts*c
        e=set()
        tm=0
        for _ in range(n):
            t=fishhook(ts,f,e)
            if t is None: break
            #print(t)
            tm+=t[2]
            #if ans!=tm:print(ts,tm-cost)
            ans=max(ans,tm-cost)
            e.add(t[1])
            ts-=t[0]
    print(ans)

def fishhook(ts,f,e):
    t=[0,0,0]
    for i in f:
        if i[1] not in e and i[0]<=ts and t[1]<i[1]:
            t=i
    return None if t==[0,0,0] else t
main()