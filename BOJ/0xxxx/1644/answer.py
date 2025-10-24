def main():
    n=int(input())
    primes=sieve_of_eratosthenes(n)
    ans=0
    i,j,psum=0,0,2
    while i<=j and j<len(primes):
        if psum<n:
            j+=1
            if j==len(primes):break
            psum+=primes[j]
        elif psum>n:
            psum-=primes[i]
            i+=1
        else:
            ans+=1
            psum-=primes[i]
            i+=1
    print(ans)
    
def sieve_of_eratosthenes(n):
    is_prime=[1]*(n+1)
    is_prime[0]=is_prime[1]=0
    for i in range(2,int(n**0.5+1)):
        if is_prime[i]:
            for j in range(i*2,n+1,i):
                is_prime[j]=0

    primes=[i for i in range(2,n+1)if is_prime[i]]
    return primes
main()