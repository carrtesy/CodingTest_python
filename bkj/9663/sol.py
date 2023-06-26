N = int(input())
cnt = 0
v = [[False]*N for _ in range(N)]

def get_moves(r, c):
  can_go = []
  for _r in range(N):
    if v[_r][c] == False:
      can_go.append((_r, c))
  for _c in range(N):
    if v[r][_c] == False:
      can_go.append((r, _c))

  dr = [1, 1, -1, -1]
  dc = [-1, 1, 1, -1]
  for i in range(4):
    _r, _c = r, c
    while 0<=_r<N and 0<=_c<N:
      if v[_r][_c] == False:
        can_go.append((_r, _c))
      _r, _c = _r+dr[i], _c+dc[i]
  return can_go

def dfs(cnt):
  print(cnt)
  if cnt == N:
    return 1
  elif cnt > N:
    return 0
    
  total_cases = 0
  for r in range(N):
    for c in range(N):
      if not v[r][c]:  
        print(f"r:{r}, c:{c}, cnt:{cnt}")
        can_go = get_moves(r, c)
        for (vr, vc) in can_go:
          v[vr][vc] = True
        for vv in v:
          print(vv)
        
        total_cases += dfs(cnt+1)

        for (vr, vc) in can_go:
          v[vr][vc] = False
          
  return total_cases

print(dfs(0))