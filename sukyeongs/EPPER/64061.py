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
