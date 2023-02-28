from collections import deque

MAX = 100001
N, K = map(int, input().split())
visited = [False] * MAX
move = [0] * MAX
q = deque([])
q.append((N, 0))
move[N] = -1
visited[N] = True

while q:
  a, t = q.popleft()
  if a == K:
    break
  if (a > 0) and (not visited[a - 1]):
    q.append((a - 1, t + 1))
    move[a - 1] = a
    visited[a - 1] = True
  if (2 * a < MAX) and (not visited[2 * a]):
    q.append((2 * a, t + 1))
    move[2 * a] = a
    visited[2 * a] = True
  if (a + 1 < MAX) and (not visited[a + 1]):
    q.append((a + 1, t + 1))
    move[a + 1] = a
    visited[a + 1] = True

path, i = [], K
while i != -1:
  path.insert(0, i)
  i = move[i]

print(t)
print(" ".join(map(str, path)))
