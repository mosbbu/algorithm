# BOJ - 9663 N-Queen
import sys
input = sys.stdin.readline

N = int(input().rstrip())
answer = 0
row = [0] * N  # row[i] = j → (i, j)에 퀸을 놓겠다

def is_possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def nqueens(x):
    global answer
    if x == N:
        answer += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_possible(x):
                nqueens(x+1)

nqueens(0)
print(answer)