import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  row = list(map(int, input().split()))
  arr.append(row)

mem = [[-1]*N for _ in range(N)]
mem[N-1][N-1] = 1

def dfs(arr, mem, r, c):
  if mem[r][c] >= 0:
    return mem[r][c]
  
  dr = [0, 1]
  dc = [1, 0]
  ans = 0
  for i in range(2):
    if arr[r][c]:
      step = arr[r][c]
      rp, cp = r+dr[i]*step, c+dc[i]*step
      if 0<=rp<N and 0<=cp<N:
        ans += dfs(arr, mem, rp, cp)
  mem[r][c] = ans
  return mem[r][c]

print(dfs(arr, mem, 0, 0))