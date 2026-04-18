def main():
    p=set()
    for inp in [*open(0)][1:]:
        name,l=inp.split()
        if l=='enter':
            p.add(name)
        else:
            p.discard(name)
    print(' '.join(sorted(p,reverse=True)))
main()