#include <iostream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n,m,i,j,k,temp,x;
    cin>>n>>m;
    vector<vector<int>> gr(n+1);
    vector<int> in_count(n+1,0);
    queue<int> q;
    vector<int> result;
    for(i=0;i<m;i++){
        cin>>k;
        for(j=0;j<k;j++){
            cin>>x;
            if(j>0){
                gr[temp].push_back(x);
                in_count[x]++;
            }
            temp=x;
        }
    }
    for(i=1;i<=n;i++){
        if(in_count[i]==0){
            q.push(i);
            result.push_back(i);
        }
    }
    while (q.size()!=0) {
        int node=q.front();q.pop();
        for(int next_node:gr[node]){
            in_count[next_node]--;
            if(in_count[next_node]==0){
                result.push_back(next_node);
                q.push(next_node);
            }
        }
    }
    if (result.size()==n){
        for (int x:result){
            cout<<x<<'\n';
        }
    }else {
        cout<<0<<'\n';
    }
    return 0;
}