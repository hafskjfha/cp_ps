def main():
    from decimal import Decimal,getcontext
    getcontext().prec=1100
    a,b=map(Decimal,input().split())
    print(f"{a**b:f}")
main()