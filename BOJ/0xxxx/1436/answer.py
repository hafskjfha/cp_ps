def find_apocalypse_number(n):
    apocalypse_numbers = [666]  # 초기값으로 666을 넣어줍니다.
    num = 666

    while len(apocalypse_numbers) < n:
        num += 1
        if '666' in str(num):  # 만약 숫자에 '666'이 포함되어 있다면 종말의 수입니다.
            apocalypse_numbers.append(num)

    return apocalypse_numbers[-1]

# 입력 받기
n = int(input())

# N번째 종말의 수 출력
print(find_apocalypse_number(n))
