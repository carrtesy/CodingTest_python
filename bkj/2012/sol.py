import sys
input = sys.stdin.readline
N = int(input())
arr = [0]
for _ in range(N):
  arr.append(int(input()))
arr.sort()
print(sum([abs(i-arr[i]) for i in range(1, N+1)]))