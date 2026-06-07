def main():
    input=open(0).readline
    n=int(input())
    a=[*map(int,input().split())]
    c1=a.count(1)
    c2=a.count(2)
    if c2>c1:print("No")
    else:print("YNeos"[(c1-c2)%3!=0::2])
    
main()