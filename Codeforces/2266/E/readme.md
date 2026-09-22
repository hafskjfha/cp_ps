# 문제 제목: [2266E Prime Destruction](https://codeforces.com/contest/2266/problem/E)
- **플랫폼**: codeforeces
- **난이도**: 4.4/10
- **풀이 유형**: DP / 정수론

---

## 1. 문제 요약
- 문제 핵심: 
  - 양의 정수 $n$개가 적혀있는 멀티셋 $A$가 있고 다음 연산을 0번이상 수행할 수 있다.
  - 연산: $A$에서 $x(x>1)$인 것을 제거한후 $x$의 소인수중 하나를 $p$라고 했을때 $A$에 $\frac{x}{p}$를 $p$개 넣는다.
  - 주어진 연산을 0번 이상 수행할 수 있을때 멀티셋의 모든 원소가 $k$이하이게 만드려고 한다. 필요한 연산횟수의 최솟값을 구하라.
- 입력/출력 조건: 
- 제한 조건: $1\le k \le n \le 2\times 10^5, 1\le a_i\le n$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $x\le k$라면 연산을 수행하지 않는게 최적임이 자명하다.
  - $x>k$인 경우라면 $x$의 소인수 $p$를 어떻게 선택하냐에 따라 달라짐을 확인하였다.
  - 예제($k=1, A=\{8,6,2,\dots\}$)를 통해 중복계산이 존재한다는 점을 확인
- 막혔던 포인트:
  - (변명) 앞선 문제로 인해 집중력이 꽤나 저하되었고 중복계산에 대해 더 파고들지 못하였다.
- 답지 참고 후:
  - $dp[x]$를 원소 하나 $x$를 시작으로, 연산을 반복하여 만들어지는 모든 원소를 $k$ 이하로 만드는 데 필요한 최소 연산 횟수라고 정의하자.
  -  $x\le k$를 이미 만족한다면 최소 연산횟수가 0이므로 그런 $x$에 대해 $dp[x]=0$으로 둘수 있다.
  - $x$의 어떤 소인수 $p_j$로 $x$를 나눈다면 1번의 연산을 사용하고 $\frac{x}{p_j}$가 $p_j$개 생긴다. 그럼 $1+p_j \times dp[\frac{x}{p_j}]$의 연산을 해야한다는 점을 알수 있다.
  - 모든 가능한 최적해의 첫 행동을 전부 열거했고, 각 첫 행동 이후의 최소 비용을 DP로 정확히 표현했기 때문에 그중에 최솟값을 선택하면 된다. 따라서 $dp[x]=1+min(p_j \times dp[\frac{x}{p_j}])$이다.

---

## 3. 코드 정리
[정답 코드](./answer.cpp)
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define all(v) (v).begin(), (v).end()

const int INF = 1e9;
const ll LINF = 1e18;


ll top_down(vector<ll> &dp,int k,int x){
    if (dp[x]!=LINF) return dp[x];

    if (x<=k){
        dp[x]=0;
        return dp[x];
    }

    int temp=x;
    if (temp%2==0){
        dp[x]=min(dp[x],1+2*top_down(dp, k, x/2));
        while (temp%2==0) {
            temp/=2;
        }
    }

    for (int i = 3; i*i <= x; i+=2) {
        if (temp%i==0){
            dp[x]=min(dp[x],1+i*top_down(dp, k, x/i));
            while (temp % i == 0) {
                temp/=i;
            }
        }
    }

    if (temp>1){
        dp[x]=min(dp[x],1+temp*top_down(dp, k, x/temp));
    }
    
    return dp[x];
}

void solve() {
    int n,k;
    cin>>n>>k;
    vector<ll> dp(n+1,LINF);
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin>>v[i];
    }

    ll ans=0;
    for(int x:v){
        ans+=top_down(dp, k, x);
    }
    cout<<ans<<'\n';
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int T = 1;
    cin >> T;

    while (T--) {
        solve();
    }

    return 0;
}
```

---

## 4. 시간/공간 복잡도

* 시간: $O(n\sqrt n)$
* 공간: $O(n)$

---

## 5. 배운 점 / 실수

* 부분 문제(중복 계산)을 dp로 환원해서 생각해보자라는 아이디어를 얻게되었다.
* 멀티셋의 정릐를 알게되었다.
* DP 점화식을 만들 때는 가능한 첫 선택을 고정후 문제가 어떤 부분 문제로 분해되는지 확인한후 모든 첫 선택 중 min/max 순서로 생각하는 아이디어를 얻게되었다.
