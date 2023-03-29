# [BOJ] 11659 - 구간 합 구하기 4
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))

for i in range(N-1):
    numList[i+1] += numList[i]
numList = [0] + numList

for _ in range(M):
    start, end = map(int, input().split())
    print(numList[end]-numList[start-1])