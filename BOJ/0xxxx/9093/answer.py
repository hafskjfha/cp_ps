for s in [*open(0)][1:]:
    print(" ".join([i[::-1] for i in s.split()]))