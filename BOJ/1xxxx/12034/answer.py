def main():
    input=open(0).readline
    for t in range(int(input())):
        n=int(input())
        ans=[]
        p=[*map(int,input().split())]
        d=dict()
        for x in p:
            d[x]=d.get(x,0)+1
        for x in p[::-1]:
            if d.get(x) and x%4==0 and d.get(x//4*3,0):
                ans.append(str(x//4*3))
                d[x//4*3]-=1
                d[x]-=1
        print(f"Case #{t+1}: {' '.join(ans[::-1])}")
main()