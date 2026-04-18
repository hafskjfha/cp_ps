def main():
    import math
    n,d=map(int,input().split())
    k=[0]*(n+1)
    for i in map(int,input().split()):
        k[i]+=1
    r=0
    for j in k:
        if j>d: r+=math.ceil((j-d)/(d-1))
    print(r)
main()