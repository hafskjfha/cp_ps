def main():
    A,B=map(int,input().split())
    cnt = 0
    i = A
    while i <= B:
        if i % 2 == 1 and i + 1 <= B:
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    print(cnt)
main()