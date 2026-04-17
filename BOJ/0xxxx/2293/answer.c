#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define ll long long

int compare(const void* a, const void* b) {
    int num1 = *(int*)a;
    int num2 = *(int*)b;
    return num1 - num2;
}

int main(void) {
    int n,k,temp;
    int arr[100],dp[10001]={0,};
    dp[0]=1;
    scanf("%d %d",&n,&k);
    for (int i = 0;i < n;i++) {
        scanf("%d",&temp);
        arr[i]=temp;
    }
    qsort(arr, n, sizeof(int), compare);
    for (int i = 0;i < n;i++) {
        for (int j = 1;j <= k;j++) {
            if(j - arr[i] < 0) continue;
            dp[j] += dp[j - arr[i]];
        }
    }
    printf("%d",dp[k]);
}