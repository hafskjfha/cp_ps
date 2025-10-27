#include <iostream>
#include <climits>
#include <vector>
#include <utility>
#include <algorithm>

#define INF LLONG_MAX

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int n,m;
    long long min_cost=INF;
    cin>>n>>m;
    vector<pair<int, int>> meat(n);
    long long now_w=0;long long now_c=0;
    int lc=-1;
    for (int i=0;i<n;i++){ cin >> meat[i].first >> meat[i].second; }
    
    sort(meat.begin(),meat.end(),[](const pair<int,int>& a, const pair<int,int>& b) {
        if (a.second == b.second)
            return a.first > b.first;  
        return a.second < b.second;    
    });
    for (auto [w,c]:meat) {
        now_w+=w;
        if (lc==c) now_c+=c;
        else now_c=c;
        lc=c;
        if(now_w>=m) min_cost=min(min_cost,now_c);
    }
    cout<<(min_cost==INF?-1:min_cost);
    return 0;
}