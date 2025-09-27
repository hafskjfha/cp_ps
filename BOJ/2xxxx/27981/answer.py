def main():
    n,k=map(int,input().split())
    if k==1:
        print(n)
    else:
        l=n.bit_length()
        a=0
        for i in range(1,l):
            a+=1+((1<<i)-1)//(1<<k)
        c=((1<<l)-1)//(1<<k)-((1<<l)-1-n)
        a+=0if c<0else c+1
        print(a)
main()
