# BOJ - 11399 ATM (solution 함수 버전)

def solution(n, line):
    line.sort()

    for i in range(1, n):
        line[i] += line[i-1]
    
    return sum(line)