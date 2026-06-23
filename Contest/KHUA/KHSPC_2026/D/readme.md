# 문제 제목: [A+B](https://dojoi.xyz/ko/problems/182)
- **플랫폼**: DOJ
- **난이도**: 3.7/10
- **풀이 유형**: 브르투포스 / 수학

---

## 1. 문제 요약
- 문제 핵심: 
  - $A+B$ 의 결과가 주어졌을때 $\text{concat}(A,B)$ 를 최대화 하는 자연수 쌍 $A,B$ 를 구하시오.
  - $\text{concat}(A,B)$ 는 $A$ 와 $B$ 를 순서대로 이어 쓴 정수이다.
- 입력/출력 조건:
- 제한 조건: $2 \le A+B \le 10^9$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $B$가 $10^k$처럼 있어야 concat한 값이 커질 것이라고 생각했다.
- 막혔던 포인트:
  - $k$를 $\lfloor \log_{10}(A+B)\rfloor$인 경우만 있다고 잘못 생각하는 바람에 계속 틀렸다.
- 답지 참고 후:
  - $B$가 $10^k$이고 $A+B\le 10^9$이기 때문에 $k=0,1,\dots,9$을 모두 해보면서 답을 구하면 되었다.

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
const ll LINF = 1e18;

void solve() {
    ll n, temp;
    cin >> n;
    ll b=1, ansb=1, maxv=(n-1)*10+1;

    for (int i = 1; i < 10; i++) {
        b*=10;
        if (b>=n) break;
        temp=(n-b)*b*10+b;
        if (maxv < temp) ansb=b; maxv=temp;

    }

    cout << n-ansb << ' ' << ansb;
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

* 시간: $O(10)$
* 공간: $O(1)$

---

## 5. 배운 점 / 실수

* $X$에 $k$꼴이 들어간 것의 최댓값을 구한것은 $k$의 범위가 작다면 완전탐색해서 최댓값을 구해야 함을 알았다.
* $k$에 한개의 값이 될 것 같다면 확실하게 증명해보는 것을 생각해봐야 겠다.
