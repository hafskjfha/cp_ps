# 문제 제목: [The Honest Woodcutters](https://atcoder.jp/contests/abc461/tasks/abc461_b)
- **플랫폼**: 앳코더
- **난이도**: 1.2/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심: 
  - $N$명의 나무꾼이 도끼를 연못에 빠뜨려 버렸고이후 $N$개의 도끼가 연못에 가라앉은 채 발견되었다.
  - 나무꾼 $i$가 $A_i$도끼가 자신 것이라고 주장한다. 반면에 연못의 여신은 도끼의 주인을 알고 있을때 모든 나무꾼이 진실을 말하고 있을까?
- 입력/출력 조건: (핵심만)
- 제한 조건: $1\le N \le 100, A_i \neq A_j, B_i \neq B_j (i \neq j)$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 리스트의 인덱싱을 이용하여 풀어 냈다.
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
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    for i in range(n):
        if b[a[i]-1]!=i+1:return print("No")
    print("Yes")
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 영어 해석을 빠르게 할 수 있도록 영어 공부를 하자. 22
