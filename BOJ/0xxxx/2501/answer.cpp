#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    vector<int>o;
    int n,k;cin>>n;
    for(int i=1;i<=n;i++){
        if(n%i==0)o.push_back(i);
    }
    cin>>k;
    cout<<(k>o.size()?0:o[k-1]);
    return 0;
}