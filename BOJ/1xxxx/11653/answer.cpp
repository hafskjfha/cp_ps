#include <iostream>
#include <math.h>
using namespace std;
int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n;cin>>n;
    if (n==1)return 0;
    for(int i=2;i<=(int)(sqrt(n));i++){
        while (n%i==0){
            cout<<i<<' ';
            n/=i;
        }
    }
    if (n>1)cout<<n;
    return 0;
}