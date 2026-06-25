# 문제 제목: [크림 먼저, 잼 먼저](https://jungol.co.kr/contest/4101/problem/3)
- **플랫폼**: Jungol
- **난이도**: 1.5/10
- **풀이 유형**: 구현

---

## 1. 문제 요약
- 문제 핵심:
  - 문자열 $T$에서 1개 이상의 `C`, 1개 이상의 `J`, 하나의 `S`가 차례대로 연속해서 나타나는 경우의 수와 1개 이상의 `J`, 1개 이상의 `C`, 하나의 `S`가 차례대로 연속해서 나타나는 경우의 수를 구하시오.
  - 중간에 문자가 하나 빠지거나 번갈아가면서 나오는 경우 (ex. `CJCS`)는 어느쪽에도 세지 않는다.
- 입력/출력 조건: 
- 제한 조건: $1 \le |T| \le 100, T$는 `C`,`S`,`J`으로만 구성된다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - `S`에 대해서 나눈후 조건에 맞는지 판정하면 된다고 생각했다.
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
    input()
    scons=input().strip().split('S')
    
    cj=jc=0
    
    for s in scons:
        temp=[]
        for c in s:
            if temp:
                if temp[-1]!=c:temp.append(c)
            else:temp.append(c)
        
        if len(temp)==2:
            if temp==['C','J']:cj+=1
            else:jc+=1
    
    print(cj,jc,sep='\n')
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(|T|)$
* 공간: $O(|T|)$

---

## 5. 배운 점 / 실수

* 구현을 효율적으로 해내자.
