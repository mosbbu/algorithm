# BOJ - 2638 치즈 (solution 함수 버전)
import sys
input = sys.stdin.readline

# N, M = map(int, input().split())
# cheese = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 치즈 외부와 내부를 구분하는 함수
def dfs(N, M, x, y):
    global cheese
    if not (0 <= x < N and 0 <= y < M) or cheese[x][y] != 0:
        return
    cheese[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(N, M, nx, ny)

def canMelt(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if cheese[nx][ny] == -1:
            cnt += 1
    return cnt >= 2

def findCheese(N, M):
    ch = list()
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1 and canMelt(i, j):
                ch.append([i, j])
    return ch

def solution(N, M, cheese):
    answer = 0
    dfs(N, M, 0, 0)
    while True:
        ch = findCheese(N, M)
        if not ch:
            break
        for c in ch:
            x, y = c
            cheese[x][y] = 0
            dfs(N, M, x, y)
        answer += 1
    return answer

cheese = [[0,0,0,0,0,0,0,0,0], [0,0,0,1,1,0,0,0,0], [0,0,0,1,1,0,1,1,0], [0,0,1,1,1,1,1,1,0], [0,0,1,1,1,1,1,0,0], [0,0,1,1,0,1,1,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
print(solution(8, 9, cheese))