# 문제 제목: [Tallest at the Moment](https://atcoder.jp/contests/abc463/tasks/abc463_c)
- **플랫폼**: 앳코더
- **난이도**: 3/10
- **풀이 유형**: 구현 / 정렬

---

## 1. 문제 요약
- 문제 핵심: 
  - 현재 회의실에 $N$명의 사람들이 있다. $i(1\le i \le N)$번째 사람은 키가 $H_i$이며 회의실을 $L_i$분 뒤에 나간다. 한번 나가면 다시는 돌아오지 않는다.
  - $Q$개의 다음과 같은 질문이 주어졌을때 각 질문에 대한 답을 구하시오.
  - 질문: $T_j + \frac{1}{2} (1\le j \le Q)$분 뒤에 남아있는 사람중 가장 키가 큰 사람의 키는 얼마인가?
- 입력/출력 조건: 
- 제한 조건: $1\le N,Q \le 3 \times 10^5, 1\le H_i \le 10^9, 1\le L_1 \le L_2 \le \cdots \le L_N \le 10^9$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $T_J$시간에 나가는 것을 처리하고 최댓값을 갱신하는 것은 $O(NQ)$으로 보였다.
  - 그래서 $L_i$보다 뒤에 나가는 사람들의 최댓값을 관리하는 배열을 관리하여 시간복잡도를 낮추려고 생각했다. 그래서 $L_i$가 큰값부터 역순으로 순회하며 최댓값을 쌓아두게 했다.
  - 회의실 배열이 $L_i$를 기준으로 정렬되어 있기때문에 $Q$개의 쿼리를 받으면서 $T_j$보다 큰 곳까지 인덱스를 높이고 정답을 갱신하게 했다.
  - 쿼리는 랜덤으로 주어지기 때문에 정렬을 진행하여 정답을 구해야 한다. 
- 막혔던 포인트:
  - x
- 답지 참고 후:
  - x

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
from collections import deque

def main():
    input=open(0).readline
    n=int(input())
    taka=sorted([[*map(int,input().split())]for _ in range(n)],key=lambda x:(x[1],x[0]))
    table=[0]*n
    for i in range(n-1,-1,-1):
        h,x=taka[i]
        table[i]=max(0 if i+1==n else table[i+1],h)
    
    tindex=0
    q=int(input())
    ans=[None]*q
    rq=sorted(enumerate(map(int,input().split())),key=lambda x:x[1])
    
    for i in range(q):
        j,t=rq[i]
        while tindex<n and taka[tindex][1]<=t:
            tindex+=1
        ans[j]=table[tindex]
    
    print("\n".join(map(str,ans)))
    
    


main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N\log N+Q\log Q)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 만약 쿼리 순서가 랜덤인 것을 의식하지 않았다면(예제에서 안줬다면) WA를 받았을 것 같은데 무언가 순서가 정해지면 그에 답이 도출될때 무조건 정렬되어야 함을 배웠다.
* 시간순으로 해결된다면 시간순 시뮬레이션이 가능한지 파악해보는 점을 배웠다.
