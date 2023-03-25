import sys
import heapq as hq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    operations = []
    heap = []

    for _ in range(k):
        operations.append(input().rstrip())
    
    for operation in operations:
        command, num = operation.split()

        if command == 'I':
            hq.heappush(heap, int(num))

        elif command == 'D' and heap:
            if num == '-1':
                hq.heappop(heap)

            elif num == '1':
                reverse_heap = [-val for val in heap]

                hq.heapify(reverse_heap)
                hq.heappop(reverse_heap)

                heap = [-val for val in reverse_heap]
                hq.heapify(heap)

    
    if heap:
        print(max(heap), min(heap))
    else:
        print('EMPTY')