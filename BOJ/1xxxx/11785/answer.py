def main():
    input=open(0).readline
    for i in range(int(input())):
        n,l=map(int,input().split())
        p=sorted(map(int,input().split()))
        s=m=t=0
        for x in p:
            if m+x>l:break
            s+=1
            m+=x
            t+=m
        print(f"Case {i+1}:",s,m,t)
main()