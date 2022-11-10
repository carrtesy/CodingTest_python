import sys

N = int(input())
arr = set(list(map(int, sys.stdin.readline().split())))
M = int(input())
query = list(map(int, sys.stdin.readline().split()))
arr.sort()

for q in query:
  ans = "yes" if q in arr else "no"
  print(ans)