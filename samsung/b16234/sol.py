import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = []
for _ in range(N):
  row = list(map(int, input().split()))
  arr.append(row)


def bfs(arr, mem, r, c, groups):
  q = deque([])
  q.append((r, c))
  dr = [0, 0, 1, -1] 
  dc = [1, -1, 0, 0]
  flag = 0
  while q:
    _r, _c = q.pop()
    for i in range(4):
      rp, cp = _r+dr[i], _c+dc[i]
      if 0<=rp<N and 0<=cp<N and mem[rp][cp] == 0: 
        if L<=abs(arr[rp][cp]-arr[_r][_c])<=R:
          flag=1
          mem[rp][cp] = groups
          q.append((rp, cp))
  if flag:
    mem[r][c] = groups
  return flag

day = 0
while True:
  mem = [[0]*N for _ in range(N)]
  
  groups = 0
  for r in range(N):
    for c in range(N):
      if mem[r][c] == 0:
        groups += bfs(arr, mem, r, c, groups+1)

  if groups == 0:
    break
  sm = [0] * (groups+1)
  gs = [[] for _ in range(groups+1)]
  for r in range(N):
    for c in range(N):
      if mem[r][c] > 0:
        gs[mem[r][c]].append((r,c))

  for g in range(1, groups+1):
    lst = gs[g]
    avg = sum([arr[a][b] for (a, b) in lst]) // len(lst)
    for (a, b) in lst:
      arr[a][b] = avg

  day += 1
      
print(day)