def main():
    input=open(0).readline
    a,b,c,d=map(int,input().split())
    if a==b:
        if a==0:
            if c>0 and d>0:
                print(-1)
            else:
                if c>0:print("1"*(c+1))
                else:print("0"*(d+1))
        else:
            print("01"+"1"*c+"01"*(a-1)+"0"*(d+1))
            
    else:
        if abs(a-b)>1:
            print(-1)
        else:
            if a>b:
                print("0"*d+"01"*a+"1"*c)
            else:
                print("1"*c+"10"*b+"0"*d)
            
        

main()