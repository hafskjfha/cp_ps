# 문제 제목: [Raise Minimum](https://atcoder.jp/contests/abc457/tasks/abc457_d)
- **플랫폼**: 앳코더
- **난이도**: 4/10
- **풀이 유형**: 이분탐색 / 매개변수탐색

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 정수 수열 $A$가 있다. 
  - 최대 $K$번 다음 연산을 수행할 수 있을때 연산을 수행 한후 $A$의 최솟값을 가장크게 만들었을때 그 값은 무엇인가?
  - 연산: $1\le i \le N$인 $i$를 골라 $A_i$에 $i$를 더한다. 
- 입력/출력 조건: 
- 제한 조건: $1\le N \le 2\times 10^5, 1 \le K \le 10^{18}$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 그리디로 가능한지 생각해보았지만 불가능해보았고 싸이클이 존재할까 생각해봤는데 안되었다.
- 막혔던 포인트:
  - $O(\log X)$ 로 시간복잡도를 깎는 방법을 생각하지 못하였다.
- 답지 참고 후:
  - 연산을 $K$번 사용하여 최솟값을 $X$로 만들 수 있는가?로 문제를 바꾸면 매개변수탐색+이분탐색으로 문제를 바꿔낼 수 있음.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
def main():
    input=open(0).readline
    n,k=map(int,input().split())
    a=[*map(int,input().split())]
    ans=-1
    
    left,right=1,4*10**18
    while left<=right:
        mid=(left+right)//2
        temp=0
        
        for i in range(n):
            need = mid - a[i]
            if need > 0:
                temp += (need + i) // (i + 1)

            if temp > k:
                break
        
        if temp<=k:
            ans=mid
            left=mid+1
        else:
            right=mid-1
            
    print(ans)
        
        

main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N\log X)$
* 공간: $O(N)$

---

## 5. 배운 점 / 실수

* 단조성을 가지는지 확인하고 가진다면 이분탐색을 고려해보자.
* 큰수를 나누는건 부동소수점 오차가 발생할 수 있으니 ceil이 포함된 연산은 $\lceil \frac{x}{d} \rceil = \lfloor \frac{x+d-1}{d} \rfloor$ 정수 나눗셈으로 풀어내자.
* * "최대의 최소값", "최소의 최대값" 형태는 답을 이분탐색할 수 있는지 먼저 확인해보자.
