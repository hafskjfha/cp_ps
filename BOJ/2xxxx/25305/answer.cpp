#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n,k;
    cin>>n>>k;
    vector<int> sc(n);
    for(int i=0;i<n;i++){
        cin>>sc[i];
    }
    sort(sc.rbegin(),sc.rend());
    cout<<sc[k-1]<<endl;
    return 0;
}