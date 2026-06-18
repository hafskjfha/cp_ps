#include <bits/stdc++.h>
#include <iostream>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define fastio ios::sync_with_stdio(false); cin.tie(nullptr)
#define all(v) (v).begin(), (v).end()

const int INF = 1e9;
const int MINF = -1e9;
const ll LINF = 1e18;
const ll MLINF = -1e18;

void solve() {
    int n, l=0;
    ll m,temp,ans,x;

    cin >> n >> m;
    vector<ll> v(n);
    
    for (int i = 0; i < n; i++) {
        cin >> temp;
        if (temp > m) continue;
        v[l]=temp;
        l++;
    }
    if (l==0){
        cout << -1;
        return;
    }

    ans=*max_element(v.begin(),v.begin()+l);

    int length = 0;
    ll tempm=m;
    while (tempm>0) {
        length++;
        tempm>>=1;
    }

    for (int i=0;i<length;i++){
        if ((m>>i)&1){
            ll temp=0,temp2=0;
            for (int j=0;j<l;j++){
                x=v[j];
                if ( ((m>>(i+1))|(x>>(i+1)))==m>>(i+1) && ((x>>i)&1)==0 ){
                    temp|=x;
                }
                if ((x&m)==x){
                    temp2|=x;
                }
                    
            }
            ans=max(ans,max(temp,temp2));
        }
    }
    cout << ans;


}

int main() {
    fastio;

    int T = 1;
    // cin >> T;

    while (T--) {
        solve();
    }

    return 0;
}