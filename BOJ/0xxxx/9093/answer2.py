for s in [*open(0)][1:]:
    for i in s.split():
        print(i[::-1],end=" ")
    print()