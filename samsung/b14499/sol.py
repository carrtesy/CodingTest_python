import sys; input = sys.stdin.readline;
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dice = [
  [0,0,0,0],
  [0,0,0,0]
]

dx = [0, 0,0,-1,1]
dy = [0, 1,-1,0,0]

def roll_dice(ord):
  if ord == 1:
    tmp = dice[0].pop(0)
    dice[0].append(tmp)
    dice[1][1], dice[1][3] = dice[0][1], dice[0][3]
  elif ord == 2:
    tmp = dice[0].pop()
    dice[0].insert(0, tmp)
    dice[1][1], dice[1][3] = dice[0][1], dice[0][3]
  elif ord == 3:
    tmp = dice[1].pop(0)
    dice[1].append(tmp)
    dice[0][1], dice[0][3] = dice[1][1], dice[1][3]
  elif ord == 4:
    tmp = dice[1].pop()
    dice[1].insert(0, tmp)
    dice[0][1], dice[0][3] = dice[1][1], dice[1][3]
  
for ord in order:
  xp, yp = x+dx[ord], y+dy[ord]
  if 0<=xp<N and 0<=yp<M:
    x, y = xp, yp
    roll_dice(ord)
    if arr[x][y] == 0:
      arr[x][y] = dice[0][3]
    else:
      dice[0][3] = dice[1][3] = arr[x][y]
      arr[x][y] = 0
    print(dice[0][1])
    