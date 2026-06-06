def main():
    input=open(0).readline
    a,d=map(int,input().split())
    print("YNeos"[a>d::2])
    
main()