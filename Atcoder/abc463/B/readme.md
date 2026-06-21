# 문제 제목: [Train Reservation](https://atcoder.jp/contests/abc463/tasks/abc463_b)
- **플랫폼**: 앳코더
- **난이도**: 1.1/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심: 
  - 기차에는 $N$개의 행 5열의 좌석이 있다. 각 열은 $A,B,C,D,E$로 불린다.
  - $X$가 주어졌을때 $X$열에 하나라도 좌석이 남아있는가를 구하시오.
- 입력/출력 조건: 
- 제한 조건: $1\le N \le 100$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 행 필터링후 남아있는 좌석이 있는지 검사했다.
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
    n,c=input().split()
    for _ in range(int(n)):
        if input().strip()[ord(c)-65]=='o':return print("Yes")
    print("No")
    


main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O( )$
* 공간: $O( )$

---

## 5. 배운 점 / 실수

* (핵심 패턴, 알고리즘 포인트, 구현 실수 등)
