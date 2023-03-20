def solution(board, moves):
    answer = 0
    stack = [0]
    
    for move in moves:
        for i in range(len(board)):        
            if board[i][move-1] == 0:
                continue
            else:
                if stack[-1] == board[i][move-1]:
                    board[i][move-1] = 0
                    stack.pop()
                    answer += 2
                    break
                else:
                    stack.append(board[i][move-1])
                    board[i][move-1] = 0
                    break
    
    return answer