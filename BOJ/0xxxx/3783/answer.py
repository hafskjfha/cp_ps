def main():
    from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
    getcontext().prec = 1000
    for i in [*open(0)][1:]:
        n = Decimal(i)
        mid=Decimal(pow(n,Decimal(1)/Decimal(3)))
        rounded_value = Decimal(mid).quantize(Decimal('1.' + '0' * 500), rounding=ROUND_HALF_UP)
        truncated_value = rounded_value.quantize(Decimal('1.0000000000'), rounding=ROUND_DOWN)
        print(truncated_value)
main()
