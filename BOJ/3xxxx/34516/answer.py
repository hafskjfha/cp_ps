def main():
    n=int(input())
    if n%4:
        print(-1)
    else:
        print('\n'.join([f'{"daaa"*(n//4)}\n{"ddab"*(n//4)}\n{"dcbb"*(n//4)}\n{"cccb"*(n//4)}'for _ in range(n//4)]))
main()