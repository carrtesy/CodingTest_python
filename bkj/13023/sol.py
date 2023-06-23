import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

ans = False

def dfs(cur, depth):
  global ans
  if depth == 5:
    ans = True
  if ans == True:
    return
    
  for nxt in graph[cur]:
    if not v[nxt]:
      v[nxt] = True
      dfs(nxt, depth+1)
      v[nxt] = False

for i in range(N):
  v = [False] * (N)
  v[i] = True
  dfs(i, 1)
  if ans:
    break
    
print(int(ans))