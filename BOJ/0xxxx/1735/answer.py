from fractions import Fraction
a=sum([Fraction(*map(int,input().split()))for _ in "11"])
print(a.numerator,a.denominator)