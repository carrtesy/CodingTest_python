from collections import deque

N = int(input())
arr = list(map(int, input().split()))

ans = 0
arr.sort()
arr = deque(arr)
group = []
while arr:
  m = arr.popleft()
  group.append(m)
  if len(group) >= group[-1]:
    ans += 1
    group = []
print(ans)