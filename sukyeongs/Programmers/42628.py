# Programmers - 42628 이중우선순위큐
from heapq import heappush, heappop, heapify

def solution(operations):
    hq = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == 'I':
            heappush(hq, int(num))
            continue
        else:
            if hq:
                if num == '1':
                    hq.remove(max(hq))
                    heapify(hq)
                    continue
                else:
                    heappop(hq)
                    continue
            else:
                continue
    if hq:
        return [max(hq), min(hq)]
    
    else:
        return [0,0]