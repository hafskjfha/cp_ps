def main():
    n=int(input())
    a,b=1,1
    for _ in range(n-1):
        c,d=(a+2*b)%9901,(a+b)%9901
        a,b=c,d
    print((a+2*b)%9901)
main()