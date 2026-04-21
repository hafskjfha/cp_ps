#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);
    int n,k,x,i,tsum,tmax=0;
    cin>>n>>k;
    vector<int> v(n);
    for(i=0;i<n;i++){
        cin>>x;
        tmax=max(tmax,x);
        v[i]=x;
    }
    sort(v.begin(),v.end());
    long mid,left=1,right=tmax;
    int ans=0;
    while(left<=right){
        tsum=0;
        mid=(left+right)/2;
        if (mid==0) break;
        for(i=0;i<n;i++){
            tsum+=v[i]/mid;
        }
        if(tsum<k){
            right=mid-1;
        } else {
            left=mid+1;
            ans=mid;
        }
    }
    cout<<ans<<endl;
    return 0;
}