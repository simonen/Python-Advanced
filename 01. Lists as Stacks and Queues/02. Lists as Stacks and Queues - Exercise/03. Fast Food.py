from collections import deque

food = int(input())
queue = deque(input().split())
print(max(list(map(int, queue))))
for i in range(len(queue)):
    order = int(queue[0])
    if food >= order:
        food -= order
        queue.popleft()
    else:
        print('Orders left:', " ".join(queue))
        break
else:
    print("Orders complete")
