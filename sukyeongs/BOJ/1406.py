# BOJ - 1406 에디터
import sys
input = sys.stdin.readline

f_str = list(input().rstrip())
b_str = []

M = int(input())

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L' and f_str:
        b_str.append(f_str.pop())
    elif cmd[0] == 'D' and b_str:
        f_str.append(b_str.pop())
    elif cmd[0] == 'B' and f_str:
        f_str.pop()
    elif cmd[0] == 'P':
        f_str.append(cmd[1])

print(''.join(f_str + b_str[::-1]))