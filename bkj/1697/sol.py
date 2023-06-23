from collections import deque
N, K = map(int, input().split())
t = 0
q = deque([(0, N)])
v = [False]*100001
while True:
  t, cur = q.popleft()
  v[cur] = True
  if cur == K:
    break
  if cur < K:
    if (0 <= 2*cur <= 100000) and not v[2*cur]:
      q.append((t+1,2*cur))
    if (0 <= cur+1 <= 100000) and not v[cur+1]:
      q.append((t+1,cur+1))
  if cur > 0:
    if (0 <= cur-1 <= 100000) and not v[cur-1]:
      q.append((t+1,cur-1))
print(t)