import sys
sys.setrecursionlimit(int(1e6+1e3))
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(lambda x:bool(int(x)), input().split())) for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, s):
  graph[r][c] = False
  s[0] += 1
  for i in range(4):
    rp, cp = r+dr[i], c+dc[i]
    if 0<=rp<n and 0<=cp<m and graph[rp][cp]:
      dfs(rp, cp, s)
  
max_area = 0
num_area = 0
for r in range(n):
  for c in range(m):
    if graph[r][c]:
      s = [0]
      dfs(r, c, s)
      max_area = max(max_area, s[0])
      num_area += 1
print(num_area)
print(max_area)