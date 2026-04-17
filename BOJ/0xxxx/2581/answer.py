def main():
    n=int(input())
    m=int(input())
    ip=[True]*(m+1)
    ip[0]=ip[1]=False
    for i in range(2,int(m**0.5)+1):
        if ip[i]:
            for j in range(i*2,m+1,i):
                ip[j]=False
    p=[k for k in range(n,m+1) if ip[k]]
    print(f"{sum(p)} {p[0]}"if p else "-1")
main()