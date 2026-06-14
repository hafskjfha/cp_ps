# 문제 제목: [쉬운 문자열 문제](https://dojoi.xyz/ko/problems/60)
- **플랫폼**: doj
- **난이도**: 3.5/10
- **풀이 유형**: 구현 / 문자열

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 문자열 $S$가 주어진다.
  - 길이가 $M$인 문자열 $T$를 만들되 $T$안에 $S$가 부분문자열로 등장하는 횟수가 최대로 되어야 할때 문자열 $T$를 구하라.
- 입력/출력 조건: 가능한 문자열이 여러개라면 아무거나 하나 출력
- 제한 조건: $1\le N,M \le 7000$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 만약 $S$가 $KK\cdots K$ 이런 꼴의 문자열(예: ddadda, aaaa)이라면 그중 가장 짧은 $K$를 선택하여 $T$는 $K$를 $\lceil \frac{M}{|K|} \rceil$만큼 반복후 남은 길이 $M - \lceil \frac{M}{|K|} \rceil$ 만큼 아무문자열을 붙이면 됩니다.
  - 만약 그런 $K$이 없다면  $\lceil \frac{M}{N} \rceil$만큼 반복후 남은 길이 $M - \lceil \frac{M}{N} \rceil$ 만큼 아무문자열을 붙이면 됩니다.
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
    n,m=map(int,input().split())
    s=input().strip()
    r=""
    
    for i in range(1,n):
        if n%i!=0:continue
        for j in range(len(s)//i-1):
            if s[i*j:i*(j+1)]!=s[i*(j+1):i*(j+2)]:break
        else:
            r=s[0:i]
            t=m//len(r)
            print(r*t+"a"*(m-len(r)*t))
            break
    else:
        print(s*(m//n)+"a"*(m-n*(m//n)))

        

main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N^2+M)$
* 공간: $O(N+M)$

---

## 5. 배운 점 / 실수

* 문자열이 최대한 많이 등장하도록 만들기 위해서는 문자열 전체를 반복하는 것이 아니라 문자열의 최소 주기를 찾아 반복해야 한다는 점을 배웠다.
