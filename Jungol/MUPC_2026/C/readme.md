# 문제 제목: [Contest Title](https://jungol.co.kr/contest/4129/problem/3)
- **플랫폼**: Jungol
- **난이도**: 1.1/10
- **풀이 유형**: 구현 / set과 map

---

## 1. 문제 요약
- 문제 핵심: 
  - `MUPC`, `MJUPC`, `MPC`, `MJPC`를 후보로 두고 투표했을때 어떤것이 표를 가장 많이 받았는지 구하라.
  - 저 4개안에 있지 않은 표는 `MUPC`로 처리된다.
- 입력/출력 조건: 가장 많은 표를 얻은게 2개 이상이라면 `REVOTE`을 출력한다.
- 제한 조건: $1\le N \le 10^5$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 각 이름당 투표수를 dict로 관리, 만약 네개의 후보중 아닌건 별도처리
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys

def main():
    input=sys.stdin.readline
    n=int(input())
    count={"MUPC":0,"MJUPC":0,"MPC":0,"MJPC":0}
    for _ in range(n):
        s=input().strip()
        if s in count:
            count[s]+=1
        else:
            count["MUPC"]+=1
    
    name,v=max(count.items(),key=lambda x:x[1])
    print("REVOTE"if [*count.values()].count(v)>1 else name)
    
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* .
