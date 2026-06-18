#include <bits/stdc++.h>
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
    int n;
    ll temp;
    cin >> n;

    unordered_map<ll, int> count;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        count[temp]++;
    }

    int maxv=MINF;
    for (auto [k,v]: count){
        maxv=max(maxv,v);
    }
    cout << max(0,2*maxv-n);

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