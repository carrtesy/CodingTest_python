import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

p = 0

for i in range(K):
  if p >= K:
    break
  a, b = A[p], B[p]
  if a < b:
    A[p], B[p] = b, a
    p += 1
  else:
    break
print(sum(A))
