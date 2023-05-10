from collections import deque

kids = deque(input().split())
toss = int(input())
while len(kids) > 1:
    kids.rotate(-toss)
    kid = kids.pop()
    print("Removed", kid)

print(f"Last is {''.join(kids)}")
