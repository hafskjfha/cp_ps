for _ in range(int(input())):
    s,*p=input().split()
    n,t,l=map(int,p)
    l*=10**8
    x=1
    if s=='O(N)':print("TLE!"if n*t>l else"May Pass.")
    if s=='O(N^2)':print("TLE!"if n**2*t>l else"May Pass.")
    if s=='O(N^3)':print("TLE!"if n**3*t>l else"May Pass.")
    if s=='O(2^N)':
        for i in range(n):
            x*=2
            if x>l:
                print('TLE!')
                break
        else:print("TLE!"if x*t>l else"May Pass.")
    if s=='O(N!)':
        for i in range(1,n+1):
            x*=i
            if x>l:
                print('TLE!')
                break
        else:print("TLE!"if x*t>l else"May Pass.")