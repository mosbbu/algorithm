# BOJ - 10808 알파벳 개수

import sys
input = sys.stdin.readline

string = input().rstrip()
alphabet = [0] * 26

for s in string:
    alphabet[ord(s)-97] += 1

print(*alphabet)