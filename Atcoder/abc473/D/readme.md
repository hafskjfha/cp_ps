# 문제 제목: [Coefficient Stair](https://atcoder.jp/contests/abc473/tasks/abc473_d)
- **플랫폼**: 앳코더
- **난이도**: 3.2/10
- **풀이 유형**: DFS / 백트래킹 / 재귀

---

## 1. 문제 요약
- 문제 핵심:
  - 길이가 $N$이고 $\sum_{i=1}^{N} i\times A_i = K$인 모든 수열을 사전순으로 출력하라.
- 입력/출력 조건: 
- 제한 조건: $1\le N\le 10, 1\le K\le 2\times10^5$, 주어진 조건을 만족하는 수열이 $3\times 10^5$보다 작음이 보장된다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - $N$이 제한이 작은 것을 보고 완전탐색$(O(2^N))$같은 알고리즘이 될 것 같았다. 또한 모든 수열을 찾는 것이기 때문에 백트래킹이라고 확신을 가졌다.
  - $0,0,\dots,0$부터 채워나가는 형식으로 재귀 트리 그래프를 만들어봤고 내 가설이 맞는 것 같았다. 하지만 정확하게 시간복잡도 바운드는 잡지 못하였다.
  - 1번째 원소부터 채워나가는 형식을 고려했으나 헷갈려서 마지막 원소부터 채워나가는 형식을 채택했다.
- 막혔던 포인트:
  - 마지막 원소부터 채워나가는 형식으로 백트래킹을 하였기 때문에 정답을 모은후 정렬을 하고 출렸했으나 틀리면서 막혔다.
- 답지 참고 후:
  - 문자열 비교를 하는 바람에 틀렸었다. 튜플로 바꿔서 정렬후 출력하니 정답을 받았다.
  - 1번쨰 원소부터 채워나가는 형식이 정답관리에 더 좋았었다.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys

input=sys.stdin.readline

n,k=map(int,input().split())
ans=[]

def back(arr,x,d):
    if d==1:
        arr[0]=x
        ans.append(tuple(arr))
        #print(arr,0,d)
        arr[0]=0
        return
    
    #print(arr,x,d)
    if x==0:
        ans.append(tuple(arr))
        return
    
    
    for i in range(1+x//d):
        arr[d-1]=i
        back(arr,x-d*i,d-1)
        
    arr[d-1]=0
    

back([0]*n,k,n)
ans.sort()
print("\n".join(" ".join(map(str,x)) for x in ans))
```

---

## 4. 시간/공간 복잡도

* 시간: $O(NM log M)$
* 공간: $O(NM+N)$

---

## 5. 배운 점 / 실수

* 문자열을 비교하는 것을 주의해야겠다고 생각했다.
* 출력순서가 정해져있다면 그 순서도 문제푸는 핵심 알고리즘에 포함된다고 생각해야겠디.