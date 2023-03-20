# BOJ - 1316 그룹 단어 체커
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for _ in range(N):
    is_group = 1
    word = input().rstrip()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                is_group = 0
                break
    if is_group == 1:
        cnt += 1
print(cnt)