# 문제 제목: [Where is my "ICP"](https://jungol.co.kr/contest/4101/problem/1)
- **플랫폼**: Jungol
- **난이도**: 1/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심: 
  - 문자열 $S$가 `ICPC`가 되게 만들고 싶을때 문자열 $T$에서 문자를 적절하게 가져와서 만들 수 있는지 구하시오.
- 입력/출력 조건: 
- 제한 조건: $1\le |S| \le 4, 1\le |T| \le 100, S$는 `ICPC`의 부분 수열이다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $S$와 $T$에서 `I`가 1개이상, `C`가 2개이상, `P`가 1개이상이면 가능하다고 생각했다.
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys
from collections import Counter

def main():
    input=sys.stdin.readline
    n=int(input())
    s=input().strip()
    m=int(input())
    t=input().strip()
    cs=Counter(s)
    ct=Counter(t)
    
    if cs.get('I',0)+ct.get('I',0)>0 and cs.get('C',0)+ct.get('C',0)>1 and cs.get('P',0)+ct.get('P',0)>0:
        print("m4us happy")
    else:
        print("m4us sad ")
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(|S|+|T|)$
* 공간: $O(|S|+|T|)$

---

## 5. 배운 점 / 실수

* .
