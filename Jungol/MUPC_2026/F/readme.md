# 문제 제목: [Flathead grey mullet](https://jungol.co.kr/contest/4129/problem/6)
- **플랫폼**: Jungol
- **난이도**: 2.4/10
- **풀이 유형**: 시뮬레이션 / 덱

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 순열 $A=1,2,\dots,N$가 있다. $A$의 길이가 0이 될때까지 다음연산을 수행한다.
    - 순열 $A$에서 가장 왼쪽에 적힌 숫자 $x$를 제거후 기록한다.
    - 만약 $x$가 이전에 제거된 숫자들보다 가장 큰 숫자라면 $A$를 뒤집는다.
    - 아직 $A$의 비지 않았다면 가장 왼쪽에 있는 숫자를 가장 오른쪽으로 옮긴다.   
  - 숫자가 제거된 순서$(c_1,c_2,\dots,c_N)$가 주어졌을떄 원래 순열 $A$를 구하시오.
- 입력/출력 조건: 
- 제한 조건: $1\le N \le 2\times 10^5$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 순열을 뒤집는 행동이 있어 BOJ 5430 AC문제를 생각하여 덱을 이용할 수 있는지 고려해보았다.
  - 먼저 인덱스 순서대로 덱을 구성한후 빼는 것을 덱으로 시뮬레이션을 하도록 했다. 
  - 시뮬레이션중 $i$가 덱에서 빠졌다면 순열이라는 조건이기 떄문에 제거 순서상 $c_t$이므로 $A_i$=$c_t$라는 것이고 만약 $c_t$가 이전에 나왔던 값보다 크다면 뒤집혔는지 체크하는 플래그를 not연산으로 바꿔주면서 처리해주면 되었다.
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
from collections import deque
import sys

def main():
    input=sys.stdin.readline
    n=int(input())
    a=[*map(int,input().split())]
    
    ans=[None]*n
    dq=deque(range(n))
    
    x_max=0
    is_reversed=False
    a_index=0
    
    while dq:
        if is_reversed:
            index=dq.pop()
        else:
            index=dq.popleft()
        ans[index]=a[a_index]
        
        if a[a_index]>x_max:
            x_max=a[a_index]
            is_reversed = not is_reversed
        
        if dq:
            if is_reversed:
                dq.appendleft(dq.pop())
            else:
                dq.append(dq.popleft())
        
        
        a_index+=1
    
    print(' '.join(map(str,ans)))


main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 문제에서 주어진 조건은 허투로 주어진 것이 아님을 상기시켰다.
* 뒤집는 연산에서는 flag와 덱을 이용해볼수 있는 지 고려함을 상기시켰다.
