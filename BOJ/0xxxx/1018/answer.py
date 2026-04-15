def count_repaints(board):

    min_repaints = float('inf')  # 최소 다시 칠해야 하는 정사각형의 개수를 저장할 변수

    

    for i in range(len(board) - 7):  # 행 인덱스

        for j in range(len(board[0]) - 7):  # 열 인덱스

            repaints_black = 0  # 검은색으로 시작하는 경우의 다시 칠해야 하는 정사각형의 개수

            repaints_white = 0  # 흰색으로 시작하는 경우의 다시 칠해야 하는 정사각형의 개수

            

            # 8x8 영역을 확인하며 체스판과 비교

            for k in range(8):  # 행 인덱스

                for l in range(8):  # 열 인덱스

                    if (k + i + l + j) % 2 == 0:  # 검은색 칸과 비교

                        if board[i + k][j + l] != 'B':

                            repaints_black += 1

                    else:  # 흰색 칸과 비교

                        if board[i + k][j + l] != 'W':

                            repaints_black += 1

                            

                    if (k + i + l + j) % 2 == 0:  # 흰색 칸과 비교

                        if board[i + k][j + l] != 'W':

                            repaints_white += 1

                    else:  # 검은색 칸과 비교

                        if board[i + k][j + l] != 'B':

                            repaints_white += 1

            

            # 최소 다시 칠해야 하는 정사각형의 개수를 업데이트

            min_repaints = min(min_repaints, repaints_black, repaints_white)

    

    return min_repaints

# 입력 받기

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

# 최소 다시 칠해야 하는 정사각형의 개수 계산

result = count_repaints(board)

print(result)

