# 문제 제목: [Gift](https://atcoder.jp/contests/abc462/tasks/abc462_b)
- **플랫폼**: 앳코더
- **난이도**: 1/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심: (짧게 2~3문장)
  - $i$번쨰 사람이 $K$명에게 선물을 주었다.
  - $i$번쨰 사람은 누구누구에게 선물을 받았는지 구하시오.
- 입력/출력 조건: 
- 제한 조건: $2\le N\le 100$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 2차원 리스트로 선물을 받은 것을 관리후 출력하였다.
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
    a=[[]for _ in range(n)]
    for i in range(n):
        _,*x=map(int,input().split())
        for y in x:
            a[y-1].append(i+1)
            
    for b in a:
        print(len(b),*b)

main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* ..
