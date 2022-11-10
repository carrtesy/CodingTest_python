import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
query = list(map(int, sys.stdin.readline().split()))
arr.sort()

print(arr)
print(query)


def binary_search(q, arr, s, e):
  if s > e:
    return "no"
  m = (s + e) // 2
  v = arr[m]
  if v < q:
    return binary_search(q, arr, m + 1, e)
  if v > q:
    return binary_search(q, arr, s, m - 1)
  else:
    return "yes"


for q in query:
  print(binary_search(q, arr, 0, N - 1))
