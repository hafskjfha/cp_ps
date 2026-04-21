import sys
def reverse_words_in_string(S):
    result = []  # 결과를 저장할 리스트
    word = []  # 현재 단어를 저장할 리스트
    in_tag = False  # 태그 내부인지 확인하는 플래그
    
    for c in S:
        if c == '<':  # 태그 시작
            if word:  # 태그 시작 전에 단어가 있으면 뒤집어서 결과에 추가
                result.append(''.join(word[::-1]))
                word = []
            in_tag = True
            result.append(c)
        elif c == '>':  # 태그 끝
            in_tag = False
            result.append(c)
        elif not in_tag and c == ' ':  # 태그 외부에서 공백을 만나면 단어 뒤집기
            if word:
                result.append(''.join(word[::-1]))
                word = []
            result.append(c)
        elif in_tag:  # 태그 내부에서는 그대로 추가
            result.append(c)
        else:  # 태그 외부에서 단어 구성
            word.append(c)
    
    if word:  # 마지막 단어 추가
        result.append(''.join(word[::-1]))
    
    return ''.join(result)

# 입력 예시
input = sys.stdin.readline
S=input().strip()
print(reverse_words_in_string(S))
