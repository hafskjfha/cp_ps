# 문제 제목: [Maximize the Gap](https://atcoder.jp/contests/abc463/tasks/abc463_d)
- **플랫폼**: 앳코더
- **난이도**: 4.8/10
- **풀이 유형**: 이분탐색 / 그리디

---

## 1. 문제 요약
- 문제 핵심: 
  - $N$개의 천이 직선에 있다. $i$번째 천은 구간 $[L_i,R_i]$를 덮는다.
  - $A$와 $B$ 천이 겹치지 않는다면 거리는 다음과 같이 정의된다: $A$천에 덮이는 임의의 점을 $p$, $B$천에 덮이는 임의의 점을 $q$라고 할때 $|p-q|$의 최솟값
  - 점수는 다음과 같이 정의된다: $K$개의 겹치지 않는 천을 선택한후 각 천들에 대한 거리의 최솟값
  - 가능한 높은 점수를 얻고 싶을때 그 점수를 구하시오.  
- 입력/출력 조건: 조건에 맞는 $K$개의 천을 고르는게 불가능하다면 -1을 출력하시오.
- 제한 조건: $2 \le K \le N \le 2\times 10^5, 0\le L_i < R_i \le 10^9$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - ~~의 최댓값을 구하는 것이라서 이분탐색을 생각했다. 결국 $X$점을 얻는게 가능하다면 $X-1$점을 얻는게 가능하기때문에 판정함수가 단조성을 띄어 가능하다고 생각했다.
- 막혔던 포인트:
  - 이분탐색의 판정함수를 효율적으로 짜는 것을 구하지 못했다.
- 답지 참고 후:
  - 판정함수중 천을 겹치지 않고 놓는다만 생각해본다면 이 문제를 Interval Scheduling Problem으로 볼수 있다. 이 문제는 먼저 끝나는 것을 선택하는 것이 최적임이 알려져 있다. 따라서 미리 천배열을 끝점을 기준으로 오름차순 정렬을 해두어야 한다.
  - 그후 판정함수에서 끝점이 작은 것 부터 선택하되 이전에 선택된 끝점+$X$가 $L_i$보다 작거나 같다면 해당 천을 선택하면 된다. 그후 선택된 천의 개수가 $K$개 이상이라면 True, 미만이라면 False를 이용하게 하면 된다.
  - 이분탐색의 범위는 $[0,10^9]$으로 하되 점수 1 이상이 불가능하다면 이는 K개의 서로 겹치지 않는 천을 고르는 것 자체가 불가능하다는 뜻이므로 -1을 출력한다.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
from collections import deque
import sys

def main():
    input=sys.stdin.readline
    n,k=map(int,input().split())
    a=sorted([tuple(map(int,input().split()))for _ in range(n)],key=lambda x:x[1])
    
    left,right=0,10**9
    ans=0
    while left<=right:
        mid=(left+right)//2
        
        count=1
        tempr=a[0][1]
        for i in range(1,n):
            l,r=a[i]
            if l>=tempr+mid:
                tempr=r
                count+=1
        
        if count>=k:
            ans=mid
            left=mid+1
        else:
            right=mid-1
            
    print(ans if ans else -1)


main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N\log N+N\log(10^9))$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* Interval Scheduling Problem문제와 어떻게 해결하는 것이 최적인지 알게되었다. (이전에 회의실 배정문제를 풀었지만 제대로 공부가 되지 않았던 것 같다.)
* 이분탐색의 사용조건과 고려해봐야 하는 문제를 다시한번 상기시키는 문제가 되었다.
