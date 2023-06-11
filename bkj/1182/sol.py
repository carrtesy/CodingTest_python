import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, 2**N):
  ans +=  (sum([arr[j] for j in range(N) if (i&2**j) >> j]) == S)
print(ans)