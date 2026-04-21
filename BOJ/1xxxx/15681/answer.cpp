#include <iostream>
#include <vector>
using namespace std;
int subtree_size[100001];

void countSubtreeNodes(int cnode,vector<vector<int>> &gr) {
    subtree_size[cnode]=1;
    for(int x:gr[cnode]){
        if (subtree_size[x]==0){
            countSubtreeNodes(x,gr);
            subtree_size[cnode]+=subtree_size[x];
        }
    }
}

int main() {
    cin.tie(NULL);cout.tie(NULL);ios_base::sync_with_stdio(false);
    int n,r,q,u,v,k;
    cin>>n>>r>>q;
    vector<vector<int>> gr(n+1);
    for(int i=0;i<n-1;i++){
        cin>>u>>v;
        gr[u].push_back(v);
        gr[v].push_back(u);
    }
    countSubtreeNodes(r,gr);
    for(int i=0;i<q;i++){
        cin>>k;
        cout<<subtree_size[k]<<'\n';
    }
    return 0;
}