#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>

using namespace std;
int main() {
    cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);
    int n,k,i;
    cin>>n>>k;
    vector<pair<int,int>> gems(n);
    vector<int> bags(k);
    priority_queue<int> pq;
    for (i=0;i<n;i++){
        cin>>gems[i].first>>gems[i].second;
    }
    for (i=0;i<k;i++){
        cin>>bags[i];
    }
    sort(gems.begin(),gems.end());
    sort(bags.begin(),bags.end());
    long ans=0;
    int gem_index=0;
    for (int bag:bags){
        while (gem_index<n && gems[gem_index].first<=bag){
            pq.push(gems[gem_index].second);
            gem_index++;
        }
        if (!pq.empty()){
            ans+=pq.top();pq.pop();
        }
    }
    cout<<ans<<endl;
    return 0;
}