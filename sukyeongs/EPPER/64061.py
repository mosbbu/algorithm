# Programmers - 64061 크레인 인형뽑기 게임
def solution(board, moves):
    doll = []
    answer = 0
    
    for move in moves:
        if board[-1][move-1] == 0:
            continue
        else:
            for top in range(len(board)):
                if board[top][move-1] == 0:
                    continue
                else:
                    if len(doll) > 0 and board[top][move-1] == doll[-1]:
                        board[top][move-1] = 0
                        doll.pop()
                        answer += 2
                        break
                    else:
                        doll.append(board[top][move-1])
                        board[top][move-1] = 0
                        break
    return answer

# 입출력 예
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))