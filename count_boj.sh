#!/bin/bash

set -euo pipefail

# usage: ./count_boj.sh [BOJ_DIRECTORY]
DIR="${1:-BOJ}"

if [ ! -d "$DIR" ]; then
  echo "폴더 '$DIR' 이(가) 존재하지 않습니다." >&2
  exit 1
fi

# BOJ 폴더 내에서 이름이 숫자(문제번호)인 모든 디렉터리 개수 세기
count=$(find "$DIR" -type d -printf '%f\n' 2>/dev/null | grep -E '^[0-9]+$' | wc -l)

echo "$count"
