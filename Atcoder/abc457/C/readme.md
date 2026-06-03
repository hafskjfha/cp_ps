# 문제 제목: [Long Sequence](https://atcoder.jp/contests/abc457/tasks/abc457_c)
- **플랫폼**: 앳코더
- **난이도**: 2/10
- **풀이 유형**: 구현 / 수학

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 정수 수열 $A,C$가 주어진다.
  - 수열 $A_i$의 길이는 $L_i$이다.
  - 수열 $A$와 $C$를 이용하여 다음 절차로 새로운 수열 B를 만든다.
    1. 처음에 $B$는 길이 0의 빈 수열이다.
    2. $i=1,2,\cdots,N$ 순서대로 다음 작업을 수행한다.
        - 수열 $A_i$를 $B$의 맨 뒤에 이어붙이는 작업을 $C_i$번 반복한다.
 - $B_K$를 구하라.
- 입력/출력 조건: 
- 제한 조건: $1\le N, 1\le L, \sum_{i=1}^{N} L_i \le 2 \times 10^5, 1\le C_i \le 10^9$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $L_i \times C_i$가 $K$보다 작다면 $K=K-L_i \times C_i$을 해주고 크다면 해당 $A_i$의 반복중 $K$가 있다는 것이므로 $A_i[K \% L_i]$을 출력하면 된다고 생각했다.
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
def main():
    input=open(0).readline
    n,k=map(int,input().split())
    a=[]
    for _ in range(n):
        _,*t=input().split()
        a.append(t)
    cs=[*map(int,input().split())]
    
    for x,y in zip(a,cs):
        if k<=len(x)*y:
            z=k%len(x)
            return print(x[z-1])
        else:
            k-=len(x)*y
    

main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 규칙을 관찰하는 아이디어
