#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int is_prime[4000000];

vector<int>sieve_of_eratosthenes(int n){
    fill(is_prime,is_prime+n+1,1);
    is_prime[0]=0;    
    is_prime[1]=0;
    for (int i=2;i<=(int)(sqrt(n));i++){
        if (is_prime[i]==1){
            for (int j=i*i;j<=n;j+=i){
                is_prime[j]=0;
            }
        }
    }
    vector<int> primes;
    for(int i=2;i<=n;i++){
        if (is_prime[i]) primes.push_back(i);
    }
    return primes;
}

int main() {
    int n;
    int ans=0;int i=0;int j=0;int psum=2;
    cin>>n;
    vector<int> primes=sieve_of_eratosthenes(n);
    while (i<=j && j<primes.size()){
        if (psum<n){
            j++;
            if (j==primes.size())break;
            psum+=primes[j];
        } else if (psum>n){
            psum-=primes[i];
            i++;
        } else {
            ans++;
            psum-=primes[i];
            i+=1;
        }
    }
    cout<<ans<<endl;
    return 0;
}