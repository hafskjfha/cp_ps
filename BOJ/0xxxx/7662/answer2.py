import heapq,os
from collections import defaultdict
heappush=heapq.heappush
heappop=heapq.heappop
input = os.read(0,1<<25).decode().splitlines().__iter__().__next__
def solve(k):
    min_heap = []
    max_heap = []
    element_count = defaultdict(int)
    
    for _ in range(k):
        op, val = input().split()
        if op == 'I':
            num = int(val)
            if element_count[num]==0:
                heappush(min_heap, num)
                heappush(max_heap, -num)
            element_count[num] += 1
        elif op == 'D':
            if val == '1':
                while max_heap and element_count[-max_heap[0]] == 0:
                    heappop(max_heap)
                if max_heap:
                    element_count[-max_heap[0]] -= 1
            elif val == '-1':
                while min_heap and element_count[min_heap[0]] == 0:
                    heappop(min_heap)
                if min_heap:
                    element_count[min_heap[0]] -= 1
    
    while max_heap and element_count[-max_heap[0]] == 0:
        heappop(max_heap)
    
    while min_heap and element_count[min_heap[0]] == 0:
        heappop(min_heap)
    
    if min_heap and max_heap:
        return f"{-max_heap[0]} {min_heap[0]}"
    else:
        return "EMPTY"

def main():
    T = int(input())
    print=os.write
    exit=os._exit
    encode=str.encode
    OK=os.EX_OK
    
    for _ in range(T):
        k = int(input())
        print(1,encode(f'{solve(k)}\n'))
    exit(OK)

main()
