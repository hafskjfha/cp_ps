# 문제 제목: [Dr. Oh](https://jungol.co.kr/contest/4129/problem/4)
- **플랫폼**: Jungol
- **난이도**: 3.8/10
- **풀이 유형**: 좌표/값압축 / 그리

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 수열 $a_1,a_2,\dots,a_N$이 있다. $w_i=2^{a_i}$라고 정의 하려고 한다.
  - 전체 $w$의 합의 $\frac{P}{Q}$이상이 되도록 수열에서 숫자를 뽑으려고 할때 뽑아야 하는 최소 개수를 구하시오.
- 입력/출력 조건: 
- 제한 조건: $1\le N \le 2\times 10^5, 1\le P \le Q \le 10^6, -10^9 \le a_i \le 10^9, 1\le i < j \le N$인 $i,j$에 대해 $|a_i - a_j|\le 20$을 만족한다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $a_i$가 큰것 부터 고르는 것이 최적이라고 생각했다.
  - $a_i$의 절댓값이 너무 커 2의 제곱을 그냥 계산하면 TLE또는 실수 오차가 발생할 것 같았다.
- 막혔던 포인트:
  - $|a_i - a_j|\le 20$ 조건을 활용하지 못해 계산 복잡성을 낮추기 못했다.
- 답지 참고 후:
  - $|a_i - a_j|\le 20$임을 이용하여 값을 압축할수 있다. 수열 $A$에서 최솟값을 $k$라고 하자. 그렇다면 지수법칙에 의해 $2^{a_i} = 2^k \cdot 2^{a_i-k}$이 되고 $2^k$는 약분이 되므로 $2^{a_i-k}$로 압축된다.
  - 또한 $a_i-k$는 양수가 되고 $\{0,1,2,\dots,20\}$에 속하는 정수이므로 직접 $2^{m}$ 형식으로 계산할 수 있다.
  - 이후 $a_i$를 압축후 계산된 $w_i$들을 내림차순으로 정렬한후 앞에서 부터 순회하면서 $Q \times \sum_{j=1}^{N}(w_j) \ge P \times \sum_{i=1}^{N}(w_i)$을 만족시키는 가장 작은 $j$를 찾고 출력하면 된다.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys

def main():
    input=sys.stdin.readline
    n,p,q=map(int,input().split())
    a=[*map(int,input().split())]
    
    mina=min(a)
    w=sorted([1<<(x-mina) for x in a],reverse=1)
    sw=sum(w)
    temp=0
    count=0
    for x in w:
        temp+=x
        count+=1
        if temp*q>=sw*p:break
    
    print(count)
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N\log N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 원소간의 제약이 있는 경우 값압축이 가능하는 점을 알게되었다.
* 비율 비교에서는 공통 배수가 약분된다는 점을 알게되었다.