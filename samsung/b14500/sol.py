import sys; input=sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tetris=[[(0,0),(0,1),(0,2),(0,3)],\
        [(0,0),(1,0),(2,0),(3,0)],\
        [(0,0),(1,0),(0,1),(1,1)],\
        [(0,0),(1,0),(2,0),(2,1)],\
        [(0,1),(1,1),(2,1),(2,0)],\
        [(0,0),(0,1),(1,1),(2,1)],\
        [(0,0),(0,1),(1,0),(2,0)],\
        [(0,0),(1,0),(1,1),(1,2)],\
        [(0,2),(1,1),(1,2),(1,0)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,1),(1,1),(1,0),(2,0)],\
        [(1,0),(1,1),(0,1),(0,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,1),(1,0),(1,1),(1,2)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,1),(1,1),(1,0),(2,1)]]
maxsum = 0
for r in range(N):
  for c in range(M):
    for t in tetris:
      ob = False
      for (x, y) in t:
        rp, cp = x+r, y+c
        if not (0<=rp<N and 0<=cp<M):
          ob = True
          break
      if ob:
        continue
      else:
        maxsum = max(maxsum, sum(map(lambda cord: arr[cord[0]+r][cord[1]+c], t)))
print(maxsum)