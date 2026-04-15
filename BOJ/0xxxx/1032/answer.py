def find_common_pattern(file_names):

    pattern = ''

    for i in range(len(file_names[0])):

        char = file_names[0][i]

        same_char = all(file_name[i] == char for file_name in file_names)

        if same_char:

            pattern += char

        else:

            pattern += '?'

    return pattern

# 입력 처리

N = int(input())

file_names = [input() for _ in range(N)]

# 공통 패턴 찾기

common_pattern = find_common_pattern(file_names)

print(common_pattern)

