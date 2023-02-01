from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
dead = []
while q:
  for i in range(K - 1):
    a = q.popleft()
    q.append(a)
  d = q.popleft()
  dead.append(d)

print("<" + ", ".join(map(str, dead)).strip() + ">")
