def main():
    input=open(0).readline
    n=int(input())
    task=sorted([tuple(map(int,input().split()))for _ in range(n)],key=lambda x:-x[1])
    v=[0]*1001
    t=0
    for d,w in task:
        for dd in range(d,0,-1):
            if v[dd]==0:
                t+=w
                v[dd]=1
                break
    print(t)
main()