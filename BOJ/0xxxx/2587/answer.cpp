#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int arr[5];
    int temp,sum=0;
    for (int i=0;i<5;i++){
        cin>>temp;
        sum+=temp;
        arr[i]=temp;
    }
    sort(arr,arr+5);
    cout<<sum/5<<' '<<arr[2]<<endl;
    return 0;
}