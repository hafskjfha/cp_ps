#include <iostream>
using namespace std;
int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int converse[101][101]={0,};
    int n,x,y,ans=0;
    cin>>n;
    for (int i=0;i<n;i++){
        cin>>x>>y;x--;y--;
        for (int dx=0;dx<10;dx++){
            for (int dy=0;dy<10;dy++){
                converse[y+dy][x+dx]=1;
            }
        }
    }
    for (int i=0;i<101;i++){
        for (int j=0;j<101;j++){
            if (converse[j][i]==1)ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}