#!/bin/bash

# 문제 번호가 입력되었는지 확인
if [ -z "$1" ]; then
    echo "사용법: $0 <문제번호>"
    exit 1
fi

PROBLEM_NO=$1

# 문제 번호를 10000으로 나눠서 폴더 그룹(ex: 0xxxx, 1xxxx)을 계산
GROUP=$((PROBLEM_NO / 10000))
DIR_PATH="BOJ/${GROUP}xxxx/${PROBLEM_NO}"

# 폴더가 이미 존재하는지 점검
if [ -d "$DIR_PATH" ]; then
    echo "존재하는 문제입니다"
else
    # 폴더 구조 재귀적 생성
    mkdir -p "$DIR_PATH"
    
    # 빈 파일(content.md, answer.py) 생성
    # touch "$DIR_PATH/content.md"
    touch "$DIR_PATH/answer.py"
    
    echo "생성 완료: $DIR_PATH"
fi