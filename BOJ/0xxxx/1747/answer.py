def s(k):
    n=1003001
    is_prime=[1]*(n+1)
    is_prime[0]=is_prime[1]=0
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2,n+1,i):
                is_prime[j]=0

    for i in range(k,n+1):
        if is_prime[i] and str(i)==str(i)[::-1]:
            return i
print(s(int(input())))