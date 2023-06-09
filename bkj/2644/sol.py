import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
v = [False] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(s, e, v, cnt):
  if s == e:
    return cnt
  ans = 999 
  for nxt in graph[s]:
    if not v[nxt]:
      v[s] = True
      ans = min(ans, dfs(nxt, e, v, cnt+1))
      v[s] = False
  return ans

ans = dfs(a, b, v, 0)
if ans == 999: ans=-1
print(ans)