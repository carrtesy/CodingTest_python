import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
  row = list(map(int, list(input().strip())))
  arr.append(row)

ans = 1
for i in range(2, N+1):
  for r in range(N-i+1):
    for c in range(M-i+1):
      if arr[r][c] == arr[r+i-1][c] == arr[r][c+i-1] == arr[r+i-1][c+i-1]:
        ans = i
        break
    if ans == i:
      break
print(ans*ans)