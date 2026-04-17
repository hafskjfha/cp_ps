#include <iostream>
using namespace std;
int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n,a;cin>>n;
    a=(1<<n)+1;
    cout<<a*a<<endl;
    return 0;
}