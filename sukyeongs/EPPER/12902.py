# Programmers - 12901 3 x n 타일링
def solution(n):
    tile = [0 for _ in range(n+2)]
    tile[2] = 3
    tile[4] = 11

    for i in range(6, n+1, 2):
        tile[i] = tile[i-2] * 3 + 2
        for j in range(i-4, -1, -2):
            tile[i] += tile[j] * 2
    return tile[n]%1000000007
