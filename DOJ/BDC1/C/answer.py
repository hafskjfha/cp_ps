def main():
    input=open(0).readline
    n=int(input())
    s=input().strip()
    if s[0]==s[-1]:return print(0)
    elif s in ("01","10"):return print(-1)
    else:
        t=n
        if s[0]=="0":
            for i in range(n):
                if s[i]=="1":
                    t=min(t,i)
                if s[n-i-1]=="0":
                    t=min(t,i)
                
        else:
            for i in range(n):
                if s[i]=="0":
                    t=min(t,i)
                if s[n-i-1]=="1":
                    t=min(t,i)
        print(t)

main()