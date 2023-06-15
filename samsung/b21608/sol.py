import sys
input = sys.stdin.readline

N = int(input())
pref = [[] for _ in range(N*N+1)]
seats = [[0] * (N+1) for _ in range(N+1)]

order = []
for _ in range(N*N):
  line = list(map(int, input().split()))
  pref[line[0]] += line[1:]
  order.append(line[0])

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for stu in order:
  cands = []
  max_likes = -1
  for r in range(1, N+1):
    for c in range(1, N+1):
      if seats[r][c]: continue
      likes = 0
      for i in range(4):
        rp, cp = r+dr[i], c+dc[i]
        if 1<=rp<=N and 1<=cp<=N and seats[rp][cp] in pref[stu]:
          likes += 1
      if likes > max_likes:
        max_likes = likes
        cands = [(r, c)]
      elif likes == max_likes:
        cands.append((r, c))

  if len(cands) == 1:
    t = cands[0]
    seats[t[0]][t[1]] = stu
    continue

  s_cands = []
  max_empty = -1 
  for (r, c) in cands:
    empty = 0
    for i in range(4):
      rp, cp = r+dr[i], c+dc[i]
      if 1<=rp<=N and 1<=cp<=N and seats[rp][cp] == 0:
        empty += 1
    if empty > max_empty:
      max_empty = empty
      s_cands = [(r, c)]
    elif empty == max_empty:
      s_cands.append((r, c))

  if len(s_cands) == 1:
    t = s_cands[0]
    seats[t[0]][t[1]] = stu
  else:
    t = min(s_cands)
    seats[t[0]][t[1]] = stu
    
satis = 0
for r in range(1, N+1):
  for c in range(1, N+1):
    stu = seats[r][c]
    n = 0
    for i in range(4):
      rp, cp = r+dr[i], c+dc[i]
      if 1<=rp<=N and 1<=cp<=N and seats[rp][cp] in pref[stu]:
        n += 1
    satis += int(10**(n-1))
print(satis)