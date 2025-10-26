#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n,m,a,b,i,node;
    cin>>n>>m;
    vector<vector<int>> gr(n+1);
    vector<int> in_count(n+1,0);
    priority_queue<int> pq;
    vector<int> result;
    for (i=0;i<m;i++){
        cin>>a>>b;
        gr[a].push_back(b);
        in_count[b]++;
    }
    for (i=1;i<=n;i++){
        if(in_count[i]==0){
            pq.push(-i);
        }
    }
    while (!pq.empty()){
        node=-pq.top();pq.pop();
        result.push_back(node);
        for(int next_node:gr[node]){
            in_count[next_node]--;
            if(in_count[next_node]==0){
                pq.push(-next_node);
            }
        }
    }
    for (int x:result){
        cout<<x<<' ';
    }
    return 0;
}