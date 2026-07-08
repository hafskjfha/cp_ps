# 문제 제목: [Yet Another Convex Hull Problem](https://doj.kr/ko/problems/344)
- **플랫폼**: DOJ
- **난이도**: 1.9/10
- **풀이 유형**: 기하학

---

## 1. 문제 요약
- 문제 핵심:
  - 좌표평면 위에 $N$개의 점이 있다. 각 점의 좌표는 $(x_i,y_i)$이다. 맨해튼 컨벡스 헐이란, 모든 점을 포함하고, 경계가 x축 또는 y축과 평행한 선분들로만 이루어진 닫힌 도형이다.
  - 주어진 모든 점을 포함하는 맨해튼 컨벡스 헐 중 둘레가 최소인 것의 둘레를 구하여라.
- 입력/출력 조건: 
- 제한 조건: $1 \le N \le 2\times 10^5, -10^9\le x_i,y_i\le 10^9$

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 가장 바깥쪽의 점들에 대해서 해당 점들을 도형의 변이 포함되게 하려고 할때 꼭짓점이 꼬불꼬불하게 되더라도 직사각형 처럼 펼수 있음을 알게되었고 그를 이용해 가장 왼/오른/위/아래 점을 기준으로 직사각형을 구성하고 둘레를 구했다.
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
    INF=float('inf')
    
    minx,maxx=INF,-INF
    miny,maxy=INF,-INF
    for _ in range(n):
        x,y=map(int,input().split())
        minx=min(minx,x)
        maxx=max(maxx,x)
        miny=min(miny,y)
        maxy=max(maxy,y)
    
    h,w=-1,-1
    if (minx>=0 and maxx>=0):
        h=maxx-minx
    elif (minx<0 and maxx<0):
        h=minx-maxx
    else:
        h=maxx-minx
    
    
    if (miny>=0 and maxy>=0):
        w=maxy-miny
    elif (miny<0 and maxy<0):
        w=miny-maxy
    else:
        w=maxy-miny
    
    print(h*2+w*2)
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(N)$
* 공간: $O(1)$

---

## 5. 배운 점 / 실수

* 지문에 그림이 있었고 그림에서는 도형의 변이 막 꼬불꼬불해서 혼란스러웠는데 유심히 생각을 해보니까 별거 아님을 알게되었다. 이를 통해 지문의 그림에 휘둘리지 않아야겠다고 생각되었다.
