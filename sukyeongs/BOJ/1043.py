# BOJ - 1043 거짓말
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 사람 수, M: 파티 수
knowList = set(input().split()[1:])
partyList = []
cnt = 0

for _ in range(M):
    partyList.append(set(input().split()[1:]))

for _ in range(M):
    for people in partyList:
        if knowList & people:
            knowList = knowList.union(people)

for people in partyList:
    if people & knowList:
        continue
    cnt += 1
print(cnt)