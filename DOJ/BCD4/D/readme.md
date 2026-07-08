# 문제 제목: [직사각형 1](https://doj.kr/ko/problems/345)
- **플랫폼**: DOJ
- **난이도**: 2.3/10
- **풀이 유형**: 수학 / dp

---

## 1. 문제 요약
- 문제 핵심: 
  - 길이가 $N$인 수열 $A$가 있고 길이가 $M$인 수열 $B$가 있다. 크기가 $N\times M$안 격자 $C$가 있고 $C_{i,j}=A_i \times B_j$이다.
  - C에서 하나의 직사각형 영역을 골라야 한다. 즉, 네 정수 $x_1,y_1,x_2,y_2(1\le x_1 \le x_2 \le N, 1\le y_1 \le y_2 \le M)$골라 $x_1 \le i \le x_2, y_1 \le j \le y_2$인 모든 $(i,j)$를 선택하여 $C$에서 해당 위치에 적혀있는 값들의 합의 최댓값을 구하시오.
- 입력/출력 조건: 
- 제한 조건: $1\le N,M \le 2\times 10^5, -10000 \le A_i,B_j \le 10000(1\le i \le N,1\le j \le M)$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 행렬곱처럼 $C$가 정의되었어서 $C$의 부분 직사각형의 합을 식으로 관찰해봤을때 $A_1B_1+A_1B_2+A_2B_1+A_2B_2=A_1(B_1+B_2)+A_2(B_1+B_2)=(A_1+A_2)(B_1+B_2)$처럼 관찰되었고 이것을 보고 $A$와 $B$의 부분합을 이용해서 A번 처럼 곱의 최댓값을 구하는 문제라고 생각했다.
- 막혔던 포인트:
  - 부분합의 최대/최소를 구하는 법을 알아내지 못하였다.
- 답지 참고 후:
  - 유명한 알고리즘인 카데인 알고리즘으로 부분합의 최대/최소를 구할 수 있었다.
  - $dp[i]$를 $i$번째 원소에서 끝나는 최대 부분합라고 정의합시다. $dp[i]=\max(dp[i-1]+A_i,A_i)$의 점화식으로 전이됩니다. 증명은 귀납법을 이용하면 증명이 가능하다고 하는데 생략하자.
  - 이를 이용해 최솟값도 별도로 구해주고 곱의 최댓값은 $\max(\min(A)\min(B),\min(A)\max(B),\max(A)\min(B),\max(A)\max(B))$으로 구할 수 있으므로 구하면 된다.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys

def main():
    INF=float('inf')
    input=sys.stdin.readline
    n,m=map(int,input().split())
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    
    submina,submaxa=subf(a,n,'m'),subf(a,n,'M')
    subminb,submaxb=subf(b,m,'m'),subf(b,m,'M')
    
    print(max(
        submaxa*submaxb,
        submina*subminb,
        submina*submaxb,
        submaxa*subminb
    ))


def subf(arr,n,k):
    fun=min if k=='m' else max
    res=arr[0]
    temp=arr[0]
    
    for i in range(1,n):
        x=arr[i]
        temp=fun(x,temp+x)
        
        if k=='M':
            if temp > res:res=temp
        else:
            if temp < res:res=temp
    
    return res
        
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N+M)$
* 공간: $O(1)$

---

## 5. 배운 점 / 실수

* 부분합의 최대/최솟값을 구하는 카데인 알고리즘에 대하여 알게되었다.
* 2차원으로 막 어려워 보이는 것을 1차원으로 어떻게 관찰할 수 있는지에 대한 아이디어를 준 문제였다.
