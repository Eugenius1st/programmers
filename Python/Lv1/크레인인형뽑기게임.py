import sys
input = sys.stdin.readline

def solution(board, moves):
    N = len(board)
    res = []
    answer = 0
    for i in moves:
        i = i-1
        if len(res) >= 2 and res[-1] == res[-2]:
            res.pop()
            res.pop()
            answer += 2

        for j in range(N):
            if board[j][i] == 0:
                continue
            else:
                res.append(board[j][i])
                board[j][i] = 0
                break
    return answer