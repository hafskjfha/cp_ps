# 문제 제목: [Variety](https://atcoder.jp/contests/abc461/tasks/abc461_c)
- **플랫폼**: 앳코더
- **난이도**: 2.5/10
- **풀이 유형**: 구현 / 정렬

---

## 1. 문제 요약
- 문제 핵심: 
  - $N$개의 보석이 있고 각 보석은 $C_i$색으로 칠해져있고 가치는 $V_i$의 가치를 가진다.
  - $K$개의 보석을 가져가서 가치를 최대화하려는데 적어도 $M$개의 다른색의 보석을 가져가야 한다. 조건에 맞게하여 보석을 가져간 최대의 가치는 얼마일까?
- 입력/출력 조건: 
- 제한 조건: $1 \le M \le K \le N \le 2 \times 10^5, 1\le C_i\le N,1\le V \le 10^9$, 적어도 $M$개의 보석은 서로 색이 다르다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 각 색의 보석마다 최댓값을 따로 저장하고 그중 가치가 큰 $M$개를 골라 가져간 후 남은 보석은 가치가 큰순서대로 $K-M$개 가져가면 된다고 생각했다.
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
    n,k,m=map(int,input().split())
    gs={}
    gm={}
    for _ in range(n):
        c,v=map(int,input().split())
        gs.setdefault(c,[]).append(v)
        gm[c]=max(gm.get(c,0),v)
    
    for key in gs.keys():gs[key].sort()
    
    sgm=sorted(gm.items(),key=lambda x:-x[1])

    
    ans=0
    for i in range(m):
        c,v=sgm[i]
        gs[c].pop()
        ans+=v
        k-=1
    
    t=[]
    if k:
        for xs in gs.values():
            t.extend(xs)
        t.sort()
        ans+=sum(t[-k:])
        
    
    print(ans)
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N \log N)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 변수명을 대충적었다가 겹쳐서 틀리는 실수를 했다. (key를 k라고 적어서 겹치는 실수)
* 문제를 어떻게 풀면되는지는 알았지만 구현이 약간 까다로웠던 것 같다.
