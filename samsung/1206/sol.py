import sys
input = sys.stdin.readline
T = 10
for t in range(1, T + 1):
  N = int(input())
  height = list(map(int, input().split()))
  ans = 0
  for i in range(2, N - 2):
    h = height[i]
    ans += max(min(h - height[i - 2], h - height[i - 1], h - height[i + 1], h - height[i + 2]), 0)
  print(f"#{t} {ans}")