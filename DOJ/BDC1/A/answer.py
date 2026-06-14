def main():
    input=open(0).readline
    n,m=map(int,input().split())
    s=input().strip()
    r=""
    
    for i in range(1,n):
        if n%i!=0:continue
        for j in range(len(s)//i-1):
            if s[i*j:i*(j+1)]!=s[i*(j+1):i*(j+2)]:break
        else:
            r=s[0:i]
            t=m//len(r)
            print(r*t+"a"*(m-len(r)*t))
            break
    else:
        print(s*(m//n)+"a"*(m-n*(m//n)))

        

main()