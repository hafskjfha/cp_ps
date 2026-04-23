#!/bin/bash

# 문제 번호가 입력되었는지 확인
if [ -z "$1" ]; then
    echo "사용법: $0 <문제번호> [확장자1,확장자2,...]"
    exit 1
fi

PROBLEM_NO=$1
EXTENSIONS=${2:-py} # 두 번째 인자가 없으면 기본값 py

# 문제 번호를 10000으로 나눠서 폴더 그룹 계산
GROUP=$((PROBLEM_NO / 10000))
DIR_PATH="BOJ/${GROUP}xxxx/${PROBLEM_NO}"

# 폴더 생성 (이미 있어도 에러 안 남)
mkdir -p "$DIR_PATH"

# 쉼표를 공백으로 치환하여 루프 돌리기
IFS=',' read -ra ADDR <<< "$EXTENSIONS"

# 각 확장자에 대해 파일 생성
for EXT in "${ADDR[@]}"; do
    EXT=$(echo $EXT | xargs) # 공백 제거
    BASE_NAME="answer"
    FILE_PATH="$DIR_PATH/$BASE_NAME.$EXT"
    
    # 중복 파일명 처리 (answer.py, answer2.py, answer3.py ...)
    COUNT=2
    FINAL_PATH=$FILE_PATH
    while [ -f "$FINAL_PATH" ]; do
        FINAL_PATH="$DIR_PATH/${BASE_NAME}${COUNT}.${EXT}"
        COUNT=$((COUNT + 1))
    done
    
    touch "$FINAL_PATH"
    echo "생성 완료: $FINAL_PATH"
done