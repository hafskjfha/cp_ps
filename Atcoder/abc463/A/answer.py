def main():
    input=open(0).readline
    x,y=map(int,input().split())
    print("YNeos"[y*16!=x*9::2])
    


main()