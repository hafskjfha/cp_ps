def main():
    from math import log,pi
    n=int(input())
    pre={1:1,2:2,6:3,24:4,120:5,720:6,5040:7,40320:8,362880:9,3628800:10,39916800:11,479001600:12,6227020800:13,87178291200:14,1307674368000:15,20922789888000:16,355687428096000:17,6402373705728000:18,121645100408832000:19}
    if n in pre: return print(pre[n])
    e=1e-3
    left,right=20,10**6
    x=log(n)
    while left<=right:
        mid=(left+right)//2
        t=mid*(log(mid)-1)+log(2*pi*mid)/2+1/(12*mid)
        if t>x+e: right=mid-1
        elif t<x-e: left=mid+1
        else: return print(mid)
            
main()