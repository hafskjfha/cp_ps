for i in [*open(0)][1:]:
    a,b=map(float,i.split())
    print(f"The height of the triangle is {2*a/b:.2f} units")