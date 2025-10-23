#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int main() {
    cin.tie(0);cout.tie(0);ios_base::sync_with_stdio(false);
    int n,q,k,c,x;
    deque<int> dq;
    cin>>n>>q>>k;
    int ss=-1,se=-1;
    bool is_reversed=false,sr=false;
    for (int i=0;i<q;i++){
        cin>>c;
        if (c==0){
            cin >> x;
            if (is_reversed){
                if (ss!=-1){ ss++;se++; }
                dq.push_front(x);
            } else {
                dq.push_back(x);
            }
        } else if (c==1){
            ss=0;se=dq.size();sr=is_reversed;
        } else{
            is_reversed=!is_reversed;
        }
    }
    if (ss!=-1){
        if (sr){
            sort(dq.begin()+ss,dq.begin()+se);
        } else{
            sort(dq.begin()+ss,dq.begin()+se,greater<int>());
        }    
    }
    
    cout<<(is_reversed?dq[k-1]:dq[dq.size()-k])<<endl;
    return 0;
}