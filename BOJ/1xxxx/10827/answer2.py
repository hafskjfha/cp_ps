def main():
    a_str,b_str=input().split()
    b=int(b_str)
    
    if '.' in a_str:
        int_part,frac_part=a_str.split('.')
        d=len(frac_part)
        X=int(int_part+frac_part)
    else:
        d=0
        X=int(a_str)

    result_int=X**b
    total_decimal_places=d*b
    result_str=str(result_int)

    if total_decimal_places>=len(result_str):
        result_str='0.'+'0'*(total_decimal_places-len(result_str))+result_str
    else:
        result_str=result_str[:-total_decimal_places]+'.'+result_str[-total_decimal_places:]
    print(result_str.rstrip('0').rstrip('.'))
main()