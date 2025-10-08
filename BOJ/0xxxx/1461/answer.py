def main():
    n,m=map(int,input().split())
    books=sorted([*map(int,input().split()),0])
    ans=0
    p=books.index(0)
    neg,pos=books[:p],books[p+1:][::-1]
    for i in range(0,len(neg),m):
        ans+=abs(neg[i])*2
    for j in range(0,len(pos),m):
        ans+=pos[j]*2
    print(ans-max(abs(books[0]),books[-1]))
main()
