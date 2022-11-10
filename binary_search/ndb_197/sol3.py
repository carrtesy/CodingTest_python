import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
query = list(map(int, sys.stdin.readline().split()))
arr.sort()

memo = [0] * 1000001
for a in arr:
  memo[a] = 1
for q in query:
  ans = "yes" if memo[q] else "no"
  print(ans)
