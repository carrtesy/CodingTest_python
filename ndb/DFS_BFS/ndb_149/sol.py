N, M = map(int, input().split())

m = []
for r in range(N):
  row = list(map(int, [*input()]))
  m.append(row)
print(m)


def dfs(m, r, c):
  drs = [1, -1, 0, 0]
  dcs = [0, 0, 1, -1]
  
  m[r][c] = 1
  for (dr, dc) in zip(drs, dcs):
    _r, _c = r+dr, c+dc
    if (0 <= _r and _r < N) and (0 <=_c and _c < M) and (not m[_r][_c]):
      dfs(m, _r, _c)

      
cnt = 0
for r in range(N):
  for c in range(M):
    if m[r][c] == 1:
      continue
    else:
      dfs(m, r, c)
      cnt += 1

print(cnt)
