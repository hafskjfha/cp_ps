def main():
    from decimal import Decimal, getcontext
    from math import ceil
    getcontext().prec = 18
    epsilon=Decimal('1e-15')
    n=input()
    if n=="0":
        print(0)
        return
    n = Decimal(n)  
    x = n / 2 
    while True:
        next_x = (x + n / x) / 2  
        if abs(next_x - x) < epsilon: 
            break
        x = next_x  
    print(ceil(next_x))
main()
