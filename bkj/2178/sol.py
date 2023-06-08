import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
  row = list(map(int, list(input().strip())))
  arr.append(row)

mem = [[10001]*M for _ in range(N)]
def dfs(arr, r, c, cnt, mem):
  mem[r][c] = min(cnt, mem[r][c])
  if r == N-1 and c == M-1:
    return
  
  dr = [1,-1,0,0]
  dc = [0,0,1,-1]
  for i in range(4):
    rp, cp = r+dr[i], c+dc[i]
    if 0<=rp<N and 0<=cp<M and arr[rp][cp]:
      if mem[rp][cp] > (mem[r][c] + 1):
        dfs(arr, rp, cp, cnt+1, mem)
  return 
dfs(arr, 0, 0, 1, mem)
print(mem[N-1][M-1])