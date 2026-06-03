# 문제 제목: [Arrays](https://atcoder.jp/contests/abc457/tasks/abc457_b)
- **플랫폼**: 앳코더 
- **난이도**: 1/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 배열 $A_1,A_2,\cdots,A_N$이 주어진다.
  - $A_i$는 길이가 $L_i$다. 즉 $A_i = (A_{i,L_1}, A_{i,L_2},\cdots,A_{i,L_i})$이다.
  - $X,Y$가 주어질때 $A_{X,Y}$를 구하라
- 입력/출력 조건: (핵심만)
- 제한 조건: $1\le N \le 2 \times 10^5, 1\le L, L$의 총합은 $2\times10^5$이 넘지 않는다. 

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 2차월 배열로 풀고 $A[X][Y]$를 출력하면 된다고 생각했다.
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
    n=int(input())
    a=[]
    for _ in range(n):
        _,*x=input().split()
        a.append(x)
    i,j=map(int,input().split())
    print(a[i-1][j-1])
    

main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(1)$
* 공간: $O(N\max(L))$

---

## 5. 배운 점 / 실수

* 영어 공부를 하면 더 빨리 풀 수 있을 것 같다. 22
