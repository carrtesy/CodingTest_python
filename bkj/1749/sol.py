import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]*(M+1)]
arr += [[0]+list(map(int, input().split())) for _ in range(N)]
print(arr)
for r in range(1, N+1):
  for c in range(2, M+1):
    arr[r][c] += arr[r][c-1]
for c in range(1, M+1):
  for r in range(2, N+1):
    arr[r][c] += arr[r-1][c]

print(arr)

ans = int(-10**9)

for r in range(1, N+1):
  for c1 in range(M):
    for c2 in range(1, M+1):
      ans = max(ans, arr[r][c2]-arr[r][c1])
      
for c in range(1, M+1):
  for r1 in range(N):
    for r2 in range(1, N+1):
      ans = max(ans, arr[r2][c]-arr[r1][c])

print(ans)