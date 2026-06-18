# 문제 제목: [서로 다른 구간 지우기](https://dojoi.xyz/ko/problems/163)
- **플랫폼**: DOJ
- **난이도**: 4.7/10
- **풀이 유형**: 그리디 / 애드혹

---

## 1. 문제 요약
- 문제 핵심:
  - 길이가 $N$인 수열 $A$에 대해서 다음 연산을 수행할 수 있다. 다음연산을 원하는 만큼 사용하여 남길 수 있는 원소 개수의 최솟값을 구하여라.
  - 현재 수열 $A$에서 두정수 $l,r$을 고른다. $l < r$이어야 하고 현재 수열의 $[l,r]$구간에 속하는 원소의 값은 모두 달라야한다. 조건을 만족한다면 $[l,r]$구간을 수열에서 삭제한다.
- 입력/출력 조건: 
- 제한 조건: $1\le N \le 2\times10^5$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 나이브하게 접근을 시도했지만 시간복잡도가 너무컸다.
- 막혔던 포인트:
  - 어떻게 구간을 설정해서 삭제해야할지 몰랐다.
- 답지 참고 후:
  - 가장 많은 게수의 원소의 개수를 $M$이라고 할때 정답은 $\max(0,2M-N)$이다.
  - $M > N/2$이라고 하고 가장 많이 등장하는 원소를 $x$라고 하자. 그럼 $x$와 $x$가 닌 원소가 접하는 부분이 최소 1개이상 존재한다. 그부분에 맞춰 $x$와 $x$가 아닌 원소를 지운다면 $x$는 $2M-N$개가 남는다.
  - $M \le N/2$라면 가장 많이 등장하는 원소를 $x$라고 하자. 그럼 $x$와 $x$가 닌 원소가 접하는 부분이 최소 1개이상 존재한다. 그부분에 대해서 $x$와 $x$가 아닌 원소를 지운다면 $M$도 한개 줄면서 $N$이 2개 줄며 최빈값은 변하지 않는다. 따라서 귀납법으로 증명할수있다.

---

## 3. 코드 정리
[정답 코드](./answer.cpp)
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define fastio ios::sync_with_stdio(false); cin.tie(nullptr)
#define all(v) (v).begin(), (v).end()

const int INF = 1e9;
const int MINF = -1e9;
const ll LINF = 1e18;
const ll MLINF = -1e18;

void solve() {
    int n;
    ll temp;
    cin >> n;

    unordered_map<ll, int> count;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        count[temp]++;
    }

    int maxv=MINF;
    for (auto [k,v]: count){
        maxv=max(maxv,v);
    }
    cout << max(0,2*maxv-n);

}

int main() {
    fastio;

    int T = 1;
    // cin >> T;

    while (T--) {
        solve();
    }

    return 0;
}
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 원소를 제거하는 연산자가 있다면 전체 수열을 보는 것보다 원소 개수에 대한 관찰을 할 수 있음을 알게되었다.
