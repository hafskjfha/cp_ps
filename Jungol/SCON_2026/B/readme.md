# 문제 제목: [숭실대입구역](https://jungol.co.kr/contest/4101/problem/2)
- **플랫폼**: Jungol
- **난이도**: 1.2/10
- **풀이 유형**: 브루트포스

---

## 1. 문제 요약
- 문제 핵심: 
  - 에스컬레이터 3개를 지나야한다. 만약 길이가 $L$인 에스컬레이터를 서서 간다면 $L$초가 걸리지만 걸어서 간다면 $\frac{L}{2}$초가 걸리지만 체력이 $\frac{L}{2}$만큼 감소한다.
  - 체력이 $H$일때 체력을 1이상남기면서 세개의 에스컬레이터를 가장 빠르게 통과할때 걸리는 시간을 구하시오.
- 입력/출력 조건: 
- 제한 조건: $2\le A,B,C\le 200, 1\le H \le 200, A,B,C$는 짝수이다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 에스컬레이터가 6개 밖에 되지 않으므로 모든 순열에 대해서 판정하면 되겠다고 생각했다.
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys
from itertools import permutations

def main():
    input=sys.stdin.readline
    p=permutations(map(int,input().split()),3)
    h=int(input())
    
    ans=float('inf')
    
    for y in p:
        temp=0
        hh=h
        for x in y:
            if hh>x//2:
                hh-=x//2
                temp+=x//2
            else:
                temp+=x
        ans=min(ans,temp)
    print(ans)
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(2^3)$
* 공간: $O(1)$

---

## 5. 배운 점 / 실수

* 경우가 작다면 브루트포스로.
