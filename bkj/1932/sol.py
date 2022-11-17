import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in range(0, n - 1):
  arr[i + 1][0] = arr[i][0] + arr[i + 1][0]
  for j in range(1, i + 1):
    arr[i + 1][j] = max(arr[i][j - 1], arr[i][j]) + arr[i + 1][j]
  arr[i + 1][i + 1] = arr[i][i] + arr[i + 1][i + 1]

print(max(arr[n - 1]))
